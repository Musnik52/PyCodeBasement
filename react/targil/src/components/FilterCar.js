import React, { Component } from "react";


class FilterCar extends Component {

    onChange = (e) => { 
        this.props.set_year_filter(e.target.value)
    }


    render() {
        //console.log(this.props);
        return (
          <div>
          <h2>Filter cars</h2>
          <p>
            Year:{" "}
            <input
              name="year"
              type="number"
              onChange={this.onChange}
              value={this.props.year_filter}
            />
          </p>
          <hr/>
          </div>
        );
      }
    }
    
    export default FilterCar;
    
