#include "gl/glut.h"
#include <cstdio>
#include "GCBezierCurve.h"

Vec2 mousePt = { 1, 0 };
float rotateAngle = 0.0;
std::vector<Vec2> ctrlPts;


void displayGlutPrimitives() {

    //glutWireSphere(1.0, 20, 20);
    //glutSolidSphere(1.0, 20, 20);

    //glutWireCube(0.5);
    //glutSolidCube(0.5);

    //glutWireCone(1.0, 1.5, 12, 12);
    //glutSolidCone(1.0, 1.5, 12, 12);

    //glutWireTorus(0.3, 0.7, 20, 20);
    //glutSolidTorus(0.3, 0.7, 20, 20);

    //glutWireTeapot(1.0);
    //glutSolidTeapot(1.0);
}

void display() {
    glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.0f, 0.0f, 0.0f);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0);   // orthogonal 투영

    //----------------- 0. Display Glut Primitives -------------------
        //displayGlutPrimitives();
    // ----------------------------------------------------------------


    //--------------- 1. Simple transform ------------------------
        //glMatrixMode(GL_MODELVIEW);
        //glColor3f(0.0f, 0.0f, 0.0f);    // 검은색
        //glLoadIdentity();   // matrix 초기화
        //glTranslatef(1.0, 0.0, 0.0);    // x방향으로 1만큼 이동, 이동한 위치에 그려줌
        //displayGlutPrimitives();

        //glColor3f(1.0, 0.0, 0.0);   // 빨간색
        //glLoadIdentity();
        //glTranslatef(0.0, 1.0, 0.0);    // y방향으로 1만큼 이동
        //displayGlutPrimitives();

        //glColor3f(0.0, 0.0, 1.0);   // 파란색
        //glLoadIdentity();
        //glTranslatef(0.0, 0.0, 1.0);    // z방향으로 1만큼 이동
        //displayGlutPrimitives();
    // ----------------------------------------------------------------


    // --------------- 2. Multiple transform --------------------------
        //glMatrixMode(GL_MODELVIEW);
        //// Rotate-Translate
        //glLoadIdentity();
        //glColor3f(1, 0, 0); // 빨간색
        //glRotatef(rotateAngle, 0.0, 0.0, 1.0);
        //glTranslatef(1.0, 0.0, 0.0);
        //displayGlutPrimitives();

        ////Translate-Rotate
        //glColor3f(0, 0, 1); // 파란색
        //glLoadIdentity();
        //glTranslatef(1.0, 0.0, 0.0);
        //glRotatef(rotateAngle, 0.0, 0.0, 1.0);
        //displayGlutPrimitives();
    // ----------------------------------------------------------------


    // --------------- 3. 2D Bezier Curve --------------------------
    BezierCurve2D curve(ctrlPts);   // vector ctrIPts

    glPointSize(10.0);
    glLineWidth(1.0);
    glColor3f(1, 0, 0);
    glBegin(GL_POINTS);
    for (auto& pt : ctrlPts)
        glVertex2f(pt.x, pt.y);
    glEnd();

    glBegin(GL_LINE_STRIP);
    for (auto& pt : ctrlPts)
        glVertex2f(pt.x, pt.y);
    glEnd();

    glColor3f(0, 0, 0);
    glLineWidth(2.0);
    glBegin(GL_LINE_STRIP);
    for (int i = 0; i <= 100; i++) {
        auto pt = curve.Evaluate(i / 100.0);    // 1~100 넣었을 때, 함수 계산, pt에 들어오는 값은 0~1
        glVertex2f(pt.x, pt.y);
    }
    glEnd();

    std::vector<float> minX, minY, maxX, maxY;
    bool increasing = true; // 기울기
    float prevX = ctrlPts.front().x, prevY = ctrlPts.front().y; // 이전 포인트 초기화

    minX.push_back(prevX);
    minY.push_back(prevY);
    maxX.push_back(prevX);
    maxY.push_back(prevY);

    for (int i = 1; i <= 100; i++) {
        auto pt = curve.Evaluate(i / 100.0);
        float dx = pt.x - prevX;
        float dy = pt.y - prevY;
        bool currIncreasing = dy / dx > 0; // 현재 기울기

        if (currIncreasing != increasing || i == 1) {
            minX.push_back(pt.x);
            minY.push_back(pt.y);
            maxX.push_back(pt.x);
            maxY.push_back(pt.y);
            increasing = currIncreasing;
        }
        else {
            size_t idx = minX.size() - 1;
            minX[idx] = std::min(minX[idx], pt.x);
            minY[idx] = std::min(minY[idx], pt.y);
            maxX[idx] = std::max(maxX[idx], pt.x);
            maxY[idx] = std::max(maxY[idx], pt.y);
        }

        prevX = pt.x; // 이전 포인트 업데이트
        prevY = pt.y;
    }

    // AABB 감싸기
    glColor3f(0, 0, 1);
    glLineWidth(2.0);
    for (size_t i = 0; i < minX.size(); i++) {
        glBegin(GL_LINE_LOOP);
        glVertex2f(minX[i], minY[i]);
        glVertex2f(maxX[i], minY[i]);
        glVertex2f(maxX[i], maxY[i]);
        glVertex2f(minX[i], maxY[i]);
        glEnd();
    }

    glutSwapBuffers();
}


void keyboard(unsigned char key, int x, int y) {

    switch (key) {
    case 27: // ESC
        exit(0);
        break;
    }
    glutPostRedisplay();
}

void special(int key, int x, int y)
{
    switch (key)
    {
    case GLUT_KEY_UP:
        rotateAngle += 10;
        break;
    case GLUT_KEY_DOWN:
        rotateAngle -= 10;
        break;
    }
    glutPostRedisplay();
}

void mouseCoordinateTranslate(int winX, int winY)
{
    mousePt.x = winX / 50.0 - 5;
    mousePt.y = (winY / 50.0 - 5) * (-1.0);
}

void changeCtrlPts()
{
    for (auto& pt : ctrlPts) {
        if (sqrt(pow(pt.x - mousePt.x, 2) + pow(pt.y - mousePt.y, 2)) < 0.5) {
            pt = mousePt;
            break;
        }
    }
}

void mouse(int button, int state, int x, int y)
{
    printf("mouse: %d %d %d %d\n", button, state, x, y);
    if (state == GLUT_DOWN) {
        mouseCoordinateTranslate(x, y);
        changeCtrlPts();
    }
    glutPostRedisplay();
}

void mouseMotion(int x, int y)
{
    printf("mouse motion: %d %d\n", x, y);
    mouseCoordinateTranslate(x, y);
    changeCtrlPts();

    glutPostRedisplay();
}

void mousePassiveMotion(int x, int y)
{
    printf("mouse passive motion: %d %d\n", x, y);
    mouseCoordinateTranslate(x, y);
    glutPostRedisplay();
}

int main(int argc, char** argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowSize(500, 500);
    glutInitWindowPosition(1480, 100);

    ctrlPts.push_back({ -2, -1 });  // Control Point
    ctrlPts.push_back({ 0, 4 });
    ctrlPts.push_back({ 2, -2 });
    ctrlPts.push_back({ 4, 2 });

    glutCreateWindow("OpenGL");
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);
    glutSpecialFunc(special);
    glutMouseFunc(mouse);
    glutMotionFunc(mouseMotion);
    //glutPassiveMotionFunc(mousePassiveMotion);
    glutMainLoop();

    return 0;
}
