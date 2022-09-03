import React, { useEffect, useState } from "react";
import axios from "axios";
import TableBoard from "../../UI/Table/TableBoard";
import Card from "../../UI/Card/Card";
import RemoveForm from "./RemoveForm";
import UserSettings from "../Airline/UserSettings";

const Airlines = (props) => {
  const colNames = ["id", "airline name", "system username"];

  const [airlineCompanies, setAirlineCompanies] = useState([]);
  const [updateAirlineId, setUpdateAirlineId] = useState("");
  const [isRemoveAction, setIsRemoveAction] = useState(false);
  const [isUpdateAction, setIsUpdateAction] = useState(false);
  const [isReturnAction, setIsReturnAction] = useState(true);

  useEffect(() => {
    axios.get(`http://localhost:8080/admins/airlines/`).then((res) => {
      setAirlineCompanies(res.data.airlines);
    });
  }, []);

  const updateAirlineHandler = (event) => {
    setUpdateAirlineId(event.target.value);
  };

  const updateActionHandler = () => {
    setIsRemoveAction(false);
    setIsReturnAction(false);
    setIsUpdateAction(true);
  };

  const removeActionHandler = () => {
    setIsUpdateAction(false);
    setIsReturnAction(false);
    setIsRemoveAction(true);
  };

  const returnActionHandler = () => {
    setIsUpdateAction(false);
    setIsRemoveAction(false);
    setIsReturnAction(true);
  };

  const submitRemoveHandler = (delData) => {
    axios
      .delete(`http://localhost:8080/admins/airlines/${delData.id}`, {
        data: { delData },
      })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  const submitUpdateHandler = (updateData) => {
    const sentAirlineData = {
      ...updateData,
      id: updateAirlineId,
    };
    axios
      .put(
        `http://localhost:8080/admins/airlines/${updateAirlineId}`,
        sentAirlineData
      )
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => console.log(err));
  };

  return (
    <React.Fragment>
      <div className="container">
        <h4 className="">Airlines</h4>
        {!isReturnAction && (
          <button
            className="btn btn-outline-info"
            onClick={returnActionHandler}
          >
            Return
          </button>
        )}
        <Card className="">
          {isReturnAction && (
            <button className="btn btn-danger" onClick={removeActionHandler}>
              Remove an Airline
            </button>
          )}
          {isReturnAction && <br />}
          {isReturnAction && (
            <button className="btn btn-success" onClick={updateActionHandler}>
              Update an Airline
            </button>
          )}
          {isRemoveAction && (
            <RemoveForm
              myInput={airlineCompanies}
              username={props.username}
              pwd={props.pwd}
              onSubmit={submitRemoveHandler}
            />
          )}
          {isUpdateAction && (
            <div className="">
              <label className="text-decoration-underline">
                Select ID # To Update
              </label>
              <br />
              <br />
              <select
                aria-label="Default select example"
                onChange={updateAirlineHandler}
              >
                <option selected value={"0"} />
                {airlineCompanies.map((c) => (
                  <option key={c.id} value={c.id}>
                    {c.id}
                  </option>
                ))}
              </select>
            </div>
          )}
        </Card>
        {isUpdateAction && (
          <UserSettings
            username={props.username}
            pwd={props.pwd}
            onUpdateAirline={submitUpdateHandler}
          />
        )}
        <TableBoard list={airlineCompanies} tableCol={colNames} />
      </div>
    </React.Fragment>
  );
};

export default Airlines;
