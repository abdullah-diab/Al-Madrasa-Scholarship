/*
1- Use a constructor function to implement a Laptop. 
  a. A laptop has a brand, model, and batteryPercentage properties. 
  b. The batteryPercentage property is the current battery level of the laptop. 

2- Implement a useSoftware method that will decrease the laptop's batteryPercentage by 15 and log the new battery level to the console.

3- Implement a charge method that will increase the laptop's batteryPercentage by 25, but it should not exceed 100. Also, log the new battery level to the console.

4- Create 2 laptop objects and experiment with calling useSoftware and charge multiple times on each of them.
*/

class Laptop {
  constructor(brand, model, batteryPercentage = 100) {
    this.brand = brand;
    this.model = model;
    this.batteryPercentage = batteryPercentage;
  }

  useSoftware() {
    if (this.batteryPercentage >= 15) {
      this.batteryPercentage -= 15;
      console.log(`Battery after opening app: ${this.batteryPercentage}%`);
    } else {
      console.log("Battery too low to open app.");
    }
  }

  charge() {
    this.batteryPercentage += 25;

    if (this.batteryPercentage > 100) {
      this.batteryPercentage = 100;
    }
    console.log(`Battery after charging: ${this.batteryPercentage}%`);
  }
}

const laptop1 = new Laptop("macbook", "pro");
const laptop2 = new Laptop("dell", "alienware");
