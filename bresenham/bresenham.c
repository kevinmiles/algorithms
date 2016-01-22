/*
   Implementation of Bresenham's line drawing
   algorithm in 4 dimensions for 3D printing
   David Yamnitsky
   */

#include <stdio.h>

#define sgn(x) (x > 0 ? 1 : (x < 0 ? -1 : 0))
#define max2(a, b) (a > b ? a : b)
#define max3(a, b, c) max2(max2(a, b), c)
#define abs(x) (x < 0 ? -x : x)

void bresenham(int x_src,
    int y_src,
    int z_src,
    int e_src,
    int x_dest,
    int y_dest,
    int z_dest,
    int e_dest,
    void (*x_step)(int dir),
    void (*y_step)(int dir),
    void (*z_step)(int dir),
    void (*e_step)(int dir))
{
  int xd, yd, zd, ed;
  int x, y, z, e;
  int ax, ay, az, ae;
  int sx, sy, sz, se;

  ax = abs(x_dest - x_src) << 1;
  ay = abs(y_dest - y_src) << 1;
  az = abs(z_dest - z_src) << 1;
  ae = abs(e_dest - e_src) << 1;

  sx = sgn(x_dest - x_src);
  sy = sgn(y_dest - y_src);
  sz = sgn(z_dest - z_src);
  se = sgn(e_dest - e_src);

  x = x_src;
  y = y_src;
  z = z_src;
  e = e_src;

  if (ax >= max3(ay, az, ae)) {

    yd = ay - (ax >> 1);
    zd = az - (ax >> 1);
    ed = ae - (ax >> 1);
    while (1) {
      if (x == x_dest)
        break;
      if (yd >= 0) {
        y += sy;
        yd -= ax;
        y_step(sy);
      }
      if (zd >= 0) {
        z += sz;
        zd -= ax;
        z_step(sz);
      }
      if (ed >= 0) {
        e += se;
        ed -= ax;
        e_step(se);
      }
      x += sx;
      yd += ay;
      zd += az;
      ed += ae;
      x_step(sx);
    }

  } else if (ay >= max3(ax, az, ae)) {

    xd = ax - (ay >> 1);
    zd = az - (ay >> 1);
    ed = ae - (ay >> 1);
    while (1) {
      if (y == y_dest)
        break;
      if (xd >= 0) {
        x += sx;
        xd -= ay;
        x_step(sx);
      }
      if (zd >= 0) {
        z += sz;
        zd -= ay;
        z_step(sz);
      }
      if (ed >= 0) {
        e += se;
        ed -= ay;
        e_step(se);
      }
      y += sy;
      xd += ax;
      zd += az;
      ed += ae;
      y_step(sy);
    }

  } else if (az >= max3(ax, ay, ae)) {

    xd = ax - (az >> 1);
    yd = ay - (az >> 1);
    ed = ae - (az >> 1);
    while (1) {
      if (z == z_dest)
        break;
      if (xd >= 0) {
        x += sx;
        xd -= az;
        x_step(sx);
      }
      if (yd >= 0) {
        y += sy;
        yd -= az;
        y_step(sy);
      }
      if (ed >= 0) {
        e += se;
        ed -= az;
        e_step(se);
      }
      z += sz;
      xd += ax;
      yd += ay;
      ed += ae;
      z_step(sz);
    }

  } else if (ae >= max3(ax, ay, az)) {

    xd = ax - (ae >> 1);
    yd = ay - (ae >> 1);
    zd = az - (ae >> 1);
    while (1) {
      if (e == e_dest)
        break;
      if (xd >= 0) {
        x += sx;
        xd -= ae;
        x_step(sx);
      }
      if (yd >= 0) {
        y += sy;
        yd -= ae;
        y_step(sy);
      }
      if (zd >= 0) {
        z += sz;
        zd -= ae;
        z_step(sz);
      }
      e += se;
      xd += ax;
      yd += ay;
      zd += az;
      e_step(se);
    }

  }
}

int x_pos;
int y_pos;
int z_pos;
int e_pos;

void x_step_cb(int dir)
{
  x_pos += dir;
  printf("(%d %d %d %d)\n", x_pos, y_pos, z_pos, e_pos);
}

void y_step_cb(int dir)
{
  y_pos += dir;
  printf("(%d %d %d %d)\n", x_pos, y_pos, z_pos, e_pos);
}

void z_step_cb(int dir)
{
  z_pos += dir;
  printf("(%d %d %d %d)\n", x_pos, y_pos, z_pos, e_pos);
}

void e_step_cb(int dir)
{
  e_pos += dir;
  printf("(%d %d %d %d)\n", x_pos, y_pos, z_pos, e_pos);
}

int main()
{
  int x_src = 0;
  int y_src = 0;
  int z_src = 0;
  int e_src = 0;
  int x_dest = 10;
  int y_dest = 10;
  int z_dest = 10;
  int e_dest = 10;

  x_pos = x_src;
  y_pos = y_src;
  z_pos = z_src;
  e_pos = e_src;

  bresenham(x_src, y_src, z_src, e_src,
      x_dest, y_dest, z_dest, e_dest,
      x_step_cb, y_step_cb, z_step_cb, e_step_cb);

  return 0;
}
