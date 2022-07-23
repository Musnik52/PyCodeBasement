import React, { Component } from "react";

class Car extends Component {
  state = {
    brand: this.props.car.brand,
    model: this.props.car.model,
    color: this.props.car.color,
    year: this.props.car.year,
    id: this.props.car.id,
    modify_mode: false,
  };
  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };
  updateClick = (e) => {
    this.props.update_car(this.state);
    this.go_to_modify_mode(e);
  };

  undoClick = (e) => {
    const car_from_papa = this.props.get_car(this.state.id);
    this.setState({
      brand: car_from_papa.brand,
      model: car_from_papa.model,
      color: car_from_papa.color,
      year: car_from_papa.year,
      modify_mode: false,
    });
  };

  go_to_modify_mode = (e) => {
    this.setState({
      modify_mode: !this.state.modify_mode,
    });
  };

  render() {
    //const brand = this.props.car.brand
    //const model = this.props.car.model
    //const color = this.props.car.color
    //const id = this.props.car.id
    // const {brand, model, color, year, id} = this.props.car

    const css1 = {
      borderRadius: "5px",
      padding: "1px",
      borderStyle: "ridge",
      border: "2px solid " + this.state.color,
      margin: "35px 50px",
    };
    if (this.state.modify_mode) {
      return (
        <div key={this.state.id} style={css1}>
          <p>
            Brand:{" "}
            <input
              type="text"
              name="brand"
              value={this.state.brand}
              onChange={this.handleChange}
            />
          </p>
          <p>
            Model:{" "}
            <input
              type="text"
              name="model"
              value={this.state.model}
              onChange={this.handleChange}
            />
          </p>
          <p>
            Year:{" "}
            <input
              type="number"
              name="year"
              value={this.state.year}
              onChange={this.handleChange}
            />
          </p>
          <p style={{ color: this.state.color }}>
            Color:{" "}
            <select
              name="color"
              id="color_id"
              value={this.state.color}
              onChange={this.handleChange}
            >
              <option value="green">Green</option>
              <option value="red">Red</option>
              <option value="orange">Orange</option>
              <option value="blue">Blue</option>
            </select>
          </p>
          <button
            style={{ color: "red" }}
            onClick={() => this.props.delete_car(this.state.id)}
          >
            X
          </button>
          &nbsp;&nbsp;
          <button style={{ color: "#F6BE00" }} onClick={this.updateClick}>
            Update
          </button>
          &nbsp;
          <button onClick={this.undoClick}>Undo</button>
        </div>
      );
    } else {
      return (
        <div key={this.state.id} style={css1}>
          <p onClick={this.go_to_modify_mode}>Brand: {this.state.brand}</p>
          <p onClick={this.go_to_modify_mode}>Model: {this.state.model}</p>
          <p onClick={this.go_to_modify_mode}>Year: {this.state.year}</p>
          <p onClick={this.go_to_modify_mode}>Color: {this.state.color}</p>
          <button
            style={{ color: "red" }}
            onClick={() => this.props.delete_car(this.state.id)}
          >
            X
          </button>
          &nbsp;&nbsp;
        </div>
      );
    }
  }
}

export default Car;
