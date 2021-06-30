import React, { useState } from "react";
import "./styles.css";

export default function App() {
  const [state, setState] = useState({
    addressType: "home",
    city: "",
    street: "",
    zipCode: "",
    houseNumber: "",
    building: "",
    toDoor: true,
    entrance: "",
    floor: "",
    apartment: "",
    info: ""
  });

  const onChange = (e) => {
    if (e.target.name === "toDoor") {
      setState({ ...state, toDoor: e.target.checked });
    } else {
      setState({ ...state, [e.target.name]: e.target.value });
    }
  };

  const submit = (e) => {
    e.preventDefault();
    console.log(state);
  };

  return (
    <div className="App">
      <h2 className="mb25">Укажите адрес доставки</h2>
      <form onSubmit={submit}>
        <div className="field mb25">
          <select
            value={state.addressType}
            onChange={onChange}
            name="addressType"
          >
            <option value="home">Дом</option>
            <option value="work">Работа</option>
            <option value="other">Другое</option>
          </select>
          <label className="label">Тип адреса</label>
        </div>
        <div className="field mb25">
          <input
            type="text"
            name="city"
            placeholder="Введите название города"
            value={state.city}
            onChange={onChange}
          />
          <label className="label">Город</label>
        </div>
        <div className="field mb25">
          <input
            type="text"
            name="street"
            placeholder="Введите название улицы"
            value={state.street}
            onChange={onChange}
          />
          <label className="label">Улица</label>
        </div>
        <div className="field__group mb25">
          <div className="field field_min">
            <input
              type="number"
              name="zipCode"
              value={state.zipCode}
              onChange={onChange}
            />
            <label className="label">Индекс</label>
          </div>
          <div className="field field_min">
            <input
              type="number"
              name="houseNumber"
              value={state.houseNumber}
              onChange={onChange}
            />
            <label className="label">Дом</label>
          </div>
          <div className="field field_min">
            <input
              type="number"
              name="building"
              value={state.building}
              onChange={onChange}
            />
            <label className="label">Корпус</label>
          </div>
        </div>
        <div className="checkbox-container mb25">
          <input
            type="checkbox"
            name="toDoor"
            id="toDoor"
            checked={state.toDoor}
            onChange={onChange}
          />
          <label className="to-door-label" htmlFor="toDoor">
            Требуется доставка до двери
          </label>
        </div>

        {state.toDoor && (
          <>
            <div className="field__group mb25">
              <div className="field field_min">
                <input
                  type="number"
                  name="entrance"
                  value={state.entrance}
                  onChange={onChange}
                />
                <label className="label">Подъезд</label>
              </div>
              <div className="field field_min">
                <input
                  type="number"
                  name="floor"
                  value={state.floor}
                  onChange={onChange}
                />
                <label className="label">Этаж</label>
              </div>
              <div className="field field_min">
                <input
                  type="number"
                  name="apartment"
                  value={state.apartment}
                  onChange={onChange}
                />
                <label className="label">Картира</label>
              </div>
            </div>
            <div className="field mb25">
              <textarea
                name="info"
                rows="4"
                placeholder="Код домофона, как пройти"
                value={state.info}
                onChange={onChange}
              />
              <label className="label">Дополнительная информация</label>
            </div>
          </>
        )}
        <button type="submit">Сохранить адрес</button>
      </form>
    </div>
  );
}
