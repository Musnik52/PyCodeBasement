import React, { Component } from "react";

class Car extends Component {
  render() {
    //const brand = this.props.brand
    //const model = this.props.model
    //const color = this.props.color
    const { brand, model, color } = this.props;
    return (
      <div>
        <p>Brand: {brand}</p>
        <p>Model: {model}</p>
        <p style={{ color }}>Color: {color} </p>
        <hr />
      </div>
    );
  }
}

export default Car;
