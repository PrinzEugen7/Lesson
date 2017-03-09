class Fubuki {
  constructor(name='吹雪', arm1='10cm連装高角砲', arm2='61cm三連装魚雷', arm3='未装備') {
    this.name = name;
    this.arm1 = arm1;
    this.arm2 = arm2;
    this.arm3 = arm3;
  }
  alertArm() {
    alert("装備1:" + this.arm1 + "\n装備2:" + this.arm2 +"\n装備3:" + this.arm3);   
  }
}

function main() {
    const fubuki = new Fubuki();
    fubuki.alertArm();
}
