import React, { Component } from "react";
import "./App.css";
import Garage from "./components/Garage";

class App extends Component {
  static my_car_seq = 4;
  state = {
    my_cars: [
      { brand: "Honda", model: "civic", color: "blue", year: 2018, id: 1 },
      {
        brand: "Ferrari",
        model: "Testa Rossa",
        color: "red",
        year: 2020,
        id: 2,
      },
      {
        brand: "Chevrolet",
        model: "cavalier",
        color: "green",
        year: 2022,
        id: 3,
      },
      { brand: "Fiat", model: "punto", color: "pink", year: 2008, id: 4 },
    ],
  };

  deleteCar = (_id) => {
    const new_cars = this.state.my_cars.filter((car) => car.id !== _id);
    this.setState({
      my_cars: new_cars,
    });
  };

  render() {
    return (
      <div className="App">
        <h1>Hello React!</h1>
        <Garage cars={this.state.my_cars} delete_car={this.deleteCar} />
      </div>
    );
  }
}

export default App;
