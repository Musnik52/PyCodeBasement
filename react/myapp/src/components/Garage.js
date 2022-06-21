import React, { Component } from "react";
import Car from "./Car";

class Garage extends Component {
  render() {
    console.log(this.props);
    return (
      <div>
        {this.props.cars.map((_car) => (
          <Car car={_car} key={_car.id} delete_car={this.props.delete_car} />
        ))}
      </div>
    );
  }
}

export default Garage;
