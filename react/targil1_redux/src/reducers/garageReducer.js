const init_state = {
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
  ],
  my_car_seq: 4,
};

const garageReducer = (state = init_state, action) => {
  console.log("------------------- my reducer");
  console.log("state:  " + JSON.stringify(state));
  console.log("action: " + JSON.stringify(action));
  if (action.type === "add_car") {
    let new_seq = state.my_car_seq;
    return {
      ...state,
      my_cars: [{ ...action.new_car, id: new_seq + 1 }, ...state.my_cars],
      my_car_seq: new_seq + 1,
    };
  }
  return state;
};

export default garageReducer;
