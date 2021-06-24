class Image extends React.Component {
  constructor(props) {
    super(props);
    this.state = { fullScreen: false };
    this.toggleFullScreen = this.toggleFullScreen.bind(this);
  }

  toggleFullScreen() {
    this.setState({ fullScreen: !this.state.fullScreen });
  }

  render() {
    const { fullScreen } = this.state;
    const className = fullScreen ? 'image image-fullscreen' : 'image';
    const buttonClassName = fullScreen ? 'btn btn-close' : 'btn btn-open';
    const style = {
      backgroundImage: `url(${this.props.src})`
    };
    return (
      <div className={className} style={style}>
        <button className={buttonClassName} onClick={this.toggleFullScreen} />
      </div>
    );
  }
}

ReactDOM.render(
  <div className="main">
    <Image src="./images/bg.png" />
  </div>,
  document.querySelector('#root')
);
