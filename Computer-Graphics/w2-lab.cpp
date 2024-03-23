#include "gl/glut.h"
#include <cstdio>

struct Vec2 {
    float x, y;
};

Vec2 linePt[4] = {
    {-0.3f, 0.2f},
    {0.6f, -0.7f},
    {-0.7f, -0.5f},
    {0.5f, 0.0f}
};

bool LineIntersect(Vec2 p1, Vec2 p2, Vec2 p3, Vec2 p4, Vec2& intersect) {
    float ua = ((p4.x - p3.x) * (p1.y - p3.y) - (p4.y - p3.y) * (p1.x - p3.x)) /
        ((p4.y - p3.y) * (p2.x - p1.x) - (p4.x - p3.x) * (p2.y - p1.y));
    float ub = ((p2.x - p1.x) * (p1.y - p3.y) - (p2.y - p1.y) * (p1.x - p3.x)) /
        ((p4.y - p3.y) * (p2.x - p1.x) - (p4.x - p3.x) * (p2.y - p1.y));

    if (ua >= 0 && ua <= 1 && ub >= 0 && ub <= 1) {
        intersect.x = p1.x + ua * (p2.x - p1.x);
        intersect.y = p1.y + ua * (p2.y - p1.y);
        return true;
    }

    return false;
}

void display() {
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    glColor3f(1.0, 0.0, 0.0);
    glBegin(GL_LINES);
    glVertex2f(linePt[0].x, linePt[0].y);
    glVertex2f(linePt[1].x, linePt[1].y);
    glEnd();

    glColor3f(0.0, 0.0, 1.0);
    glBegin(GL_LINES);
    glVertex2f(linePt[2].x, linePt[2].y);
    glVertex2f(linePt[3].x, linePt[3].y);
    glEnd();

    /* Calculate the intersection point */
    glColor3f(0.0, 1.0, 0.0);
    glPointSize(10.0);
    glBegin(GL_POINTS);

    Vec2 intersect;
    if (LineIntersect(linePt[0], linePt[1], linePt[2], linePt[3], intersect)) {
        glVertex2f(intersect.x, intersect.y);
    }

    glEnd();
    glutSwapBuffers();
}

void keyboard(unsigned char key, int x, int y) {

    switch (key) {
    case 'w':
        linePt[0].y += 0.1f;
        linePt[1].y += 0.1f;
        break;
    case 's':
        linePt[0].y -= 0.1f;
        linePt[1].y -= 0.1f;
        break;
    case 'a':
        linePt[0].x -= 0.1f;
        linePt[1].x -= 0.1f;
        break;
    case 'd':
        linePt[0].x += 0.1f;
        linePt[1].x += 0.1f;
        break;
    case 27: // ESC
        exit(0);
        break;
    }
    glutPostRedisplay();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(1480, 100);

    glutCreateWindow("OpenGL");
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutMainLoop();

    return 0;
}
