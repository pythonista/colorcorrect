#ifndef COLORCORRECT_CUTIL_CUTIL_H_
#define COLORCORRECT_CUTIL_CUTIL_H_
#include <stdlib.h>

extern "C"{
  typedef struct {
    int width;
    int height;
    unsigned char *r;
    unsigned char *g;
    unsigned char *b;
  } rgbimage_t;

  double* calc_sdlwgw(rgbimage_t* img, int subwidth, int subheight);
  double* calc_lwgw(rgbimage_t* img, int subwidth, int subheight);
  void calc_ace(rgbimage_t* img);
  void delete_doubleptr(double* p);
}

#endif