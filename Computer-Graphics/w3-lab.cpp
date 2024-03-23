#include "gl/glut.h"
#include <cstdio>
#include <vector>
using namespace std;

struct Vec2 {
    float x, y;
};

struct Line {
    vector<Vec2> points;
    float thick;
};

vector<Line> lines; 
vector<Vec2> currentLine;
float penThick = 1.0f;

void display() {
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    glColor3f(0.0f, 0.0f, 0.0f);
    for (const auto& line : lines) {
        glLineWidth(line.thick);
        glBegin(GL_LINE_STRIP);
        for (const auto& point : line.points) {
            glVertex2f(point.x, point.y);
        }
        glEnd();
    }

    if (!currentLine.empty()) {
        glLineWidth(penThick);
        glBegin(GL_LINE_STRIP);
        for (const auto& point : currentLine) {
            glVertex2f(point.x, point.y);
        }
        glEnd();
    }

    glutSwapBuffers();
}

void keyboard(unsigned char key, int x, int y) {
    switch (key) {
    case '1':
        penThick = 1.0f;
        break;
    case '2':
        penThick = 2.0f;
        break;
    case '3':
        penThick = 3.0f;
        break;
    case '4':
        penThick = 4.0f;
        break;
    case '5':
        penThick = 5.0f;
        break;
    case 'r':
        lines.clear();
        break;
    case 27: // ESC
        exit(0);
        break;
    }
    glutPostRedisplay();
}

void mouseCoordinateTranslate(int winX, int winY) {
    Vec2 point;
    point.x = winX / 250.0 - 1;
    point.y = (winY / 250.0 - 1) * (-1.0);
    currentLine.push_back(point);
}

void mouse(int button, int state, int x, int y) {
    if (state == GLUT_DOWN) {
        currentLine.clear();
        mouseCoordinateTranslate(x, y);
    }
    else if (state == GLUT_UP) {
        if (!currentLine.empty()) {
            lines.push_back({currentLine, penThick});
            currentLine.clear();
        }
    }
    glutPostRedisplay();
}

void mouseMotion(int x, int y) {
    mouseCoordinateTranslate(x, y);
    glutPostRedisplay();
}

void mousePassiveMotion(int x, int y)
{
    printf("mouse passive motion: %d %d\n", x, y);
    mouseCoordinateTranslate(x, y);
    glutPostRedisplay();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(1480, 100);

    glutCreateWindow("OpenGL");
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMouseFunc(mouse);
    glutMotionFunc(mouseMotion);
    //glutPassiveMotionFunc(mousePassiveMotion);
    glutMainLoop();

    return 0;
}
