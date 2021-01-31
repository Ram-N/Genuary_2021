//Code Source: The coding train
//Adapted for Genuary2021.

// Fluid Simulation
// Daniel Shiffman
// https://thecodingtrain.com/CodingChallenges/132-fluid-simulation.html
// https://youtu.be/alhpH6ECFvQ

// This would not be possible without:
// Real-Time Fluid Dynamics for Games by Jos Stam
// http://www.dgp.toronto.edu/people/stam/reality/Research/pdf/GDC03.pdf
// Fluid Simulation for Dummies by Mike Ash
// https://mikeash.com/pyblog/fluid-simulation-for-dummies.html

final int N = 512;
final int iter = 16;
final int SCALE = 1;
float t = 0;

Fluid fluid;

void settings() {
  size(N*SCALE, N*SCALE);
}

void setup() {
  fluid = new Fluid(0.2, 0, 0.000001);
}

//void mouseDragged() {
//}

void draw() {
  background(0);
  int cx = int(0.5*width/SCALE);
  int cy = int(0.5*height/SCALE);
  for (int i = -1; i <= 1; i++) {
    for (int j = -1; j <= 1; j++) {
      for (int k = 1; k <= 4; k+=1) {    
        fluid.addDensity(cx+i*width/9+k, cy+j*height/9+k, random(50, 150));
      }
    }
  }
  for (int i = 0; i < 2; i++) {
    float angle = noise(t) * TWO_PI * 2;
    PVector v = PVector.fromAngle(angle);
    v.mult(0.2);
    t += 0.01;
    fluid.addVelocity(cx, cy, v.x, v.y );
  }


  fluid.step();
  fluid.renderD();
  //fluid.renderV();
  //fluid.fadeD();
  noFill();
  stroke(255);
  strokeWeight(20);
  rect(0,0,width,height);
  if (frameCount % 100 == 0){
    saveFrame("images/6_####.png");
  }
}
