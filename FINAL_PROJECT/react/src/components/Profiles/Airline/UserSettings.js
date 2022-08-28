import React, { useEffect, useState } from "react";
import Card from "../../UI/Card/Card";
import Button from "../../UI/Button/Button";
import axios from "axios";
import "./UserUpdate.css";

const UserSettings = (props) => {
  const [enteredName, setEnteredName] = useState("");
  const [enteredCountryId, setEnteredCountryId] = useState("");
  const [enteredUserId, setUserId] = useState("");
  const [enteredAirlineId, setAirlineId] = useState("");
  const [myCountries, setMyCountries] = useState([]);

  useEffect(() => {
    axios
      .get(`http://localhost:8080/airlines/${props.username}`)
      .then((res) => {
        console.log(res.data.airline);
        setEnteredName(res.data.airline.name);
        setEnteredCountryId(res.data.airline.country_id);
        setUserId(res.data.airline.user_id);
        setAirlineId(res.data.airline.id);
      });
      axios.get(`http://localhost:8080/countries`).then((res) => {
        setMyCountries(res.data.countries);
      });
  }, []);


  const NameChangeHandler = (event) => {
    setEnteredName(event.target.value);
  };

  const countryIdChangeHandler = (event) => {
    setEnteredCountryId(event.target.value);
  };

  const submitHandler = (event) => {
    event.preventDefault();

    const updateData = {
      username: props.username,
      password: props.pwd,
      id: enteredAirlineId,
      name: enteredName,
      countryId: enteredCountryId,
      UserId: enteredUserId,
    };

    axios
      .put(`http://localhost:8080/airlines/${props.username}`, updateData)
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  const deleteHandler = (event) => {
    axios
      .delete(`http://localhost:8080/airlines/${props.username}`, {
        data: { pwd: props.pwd },
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
    return props.onLogout();
  };

  return (
    <Card className="update">
      <h4 className="">User Settings</h4>
      <form onSubmit={submitHandler}>
        <div className="new-airline__controls">
          <div className="new-airline__control">
            <label className="control">Name</label>
            <input
              className="control"
              type="text"
              value={enteredName}
              onChange={NameChangeHandler}
            />
          </div>
          <div className="new-airline__control">
            <label className="control">Country</label>
            <select
              className="form-select"
              aria-label="Default select example"
              onChange={countryIdChangeHandler}
            >
              <option selected value={0}>
                Choose a country
              </option>
              {myCountries.map((c) => (
                <option key={c.id} value={c.id}>
                  {c.name}
                </option>
              ))}
            </select>
          </div>
          <div className="new-airline__control">
            <label className="control">Delete Profile</label>
            <button
              className="btn btn-danger delete_airline"
              type="button"
              onClick={deleteHandler}
            >
              Press Here To Delete
            </button>
          </div>
        </div>
        <div className="new-airline__actions">
          <Button type="submit">Update</Button>
        </div>
      </form>
    </Card>
  );
};

export default UserSettings;
