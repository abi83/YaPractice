import React from 'react';
import formStyles from './form.module.css';

class Form extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isSubmit: false,
      value: ''
    };
    this.emailInput = React.createRef();
    this.handleFormSubmit = this.handleFormSubmit.bind(this);
  }
  handleFormSubmit(e) {
    e.preventDefault();
    console.log(e);
    this.setState({...this.state, isSubmit: true, value: this.emailInput.current.value})
  }
  componentDidMount() {
    this.emailInput.current.focus();
  }
  render() {
    const successMessage = `
      <>
        <span>Почта {this.state.value} успешно подписана на рассылку</span>
        <span>Но это не точно</span>
      </>
    `
    return (
      <div className={formStyles.root}>
        <form
          className={formStyles.form}
          onSubmit={this.handleFormSubmit}
        >
          <input
            className={formStyles.input}
            type='email'
            placeholder={'Введите свой e-mail'}
            ref={this.emailInput}
          />
          <button
            className={formStyles.button}
            type={'submit'}
          >
            Подписаться
          </button>
        </form>
        <p className={formStyles.message}>
          {this.state.isSubmit && successMessage}
        </p>
      </div>
    );
  }
}

export default Form;
