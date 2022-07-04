import React, { Component } from "react";

class AddCar extends Component {
  state = {
    car_form_input: {
      brand: "",
      model: "",
      year: "",
      color: "green",
    },
  };

  handleChange = (e) => {
    console.log(e.target.name);
    console.log(e);
    const new_value = { ...this.state.car_form_input };
    new_value[e.target.name] = e.target.value;
    console.log(new_value);

    // workaround for the spread operator
    //let new_car_form_input = Object.assign({}, this.state.car_form_input);
    //new_car_form_input [e.target.name] = e.target.value
    //this.setState({
    //car_form_input:new_car_form_input
    //})

    this.setState({
      car_form_input: {
        ...this.state.car_form_input,
        [e.target.name]: e.target.value,
      },
    });
  };

  handleSubmit = (e) => {
    // default action is page refresh. we want to prevent that.
    e.preventDefault(); 
    //  it's simple JS
    console.log('form submitted', this.state.car_form_input);
    this.props.add_car(this.state.car_form_input)
  }

  render() {
    //this.props.car

    return (
      <div>
        <h2>New car</h2>
        <form onSubmit={this.handleSubmit}>
          <p>
            Brand:{" "}
            <input
              name="brand"
              type="text"
              onChange={this.handleChange}
              value={this.state.car_form_input.brand}
              required
            />
          </p>
          <p>
            Model:{" "}
            <input
              name="model"
              type="text"
              onChange={this.handleChange}
              value={this.state.car_form_input.model}
              required
            />
          </p>
          <p>
            Year:{" "}
            <input
              name="year"
              type="number"
              onChange={this.handleChange}
              value={this.state.car_form_input.year}
              required
            />
          </p>
          <p>
            Color:{" "}
            <select
              name="color"
              id="color_id"
              onChange={this.handleChange}
              value={this.state.car_form_input.color}
            >
              <option value="green">Green</option>
              <option value="red">Red</option>
              <option value="orange">Orange</option>
              <option value="blue">Blue</option>
            </select>
          </p>
          <button type="submit">Buy New Car</button>
        </form>
        <hr />
      </div>
    );
  }
}

export default AddCar;
