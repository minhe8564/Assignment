#include "GL/glut.h"

void display() {
	glClearColor(1.0f, 1.0f, 1.0f, 1.0f);
	glClear(GL_COLOR_BUFFER_BIT);

	glColor3f(0.0f, 1.0f, 1.0f);	// 0.0 ~ 1.0
	glLineWidth(5.0);
	glBegin(GL_LINE_LOOP);
	glVertex2f(0, 0);
	glVertex2f(0.5, 0);
	glVertex2f(0.5, 0.5);
	glEnd();

	glFinish();
}

int main(int argc, char** argv) {
	glutInit(&argc, argv);
	glutCreateWindow("OpenGL");
	glutDisplayFunc(display);
	glutMainLoop();
	return 0;
}
