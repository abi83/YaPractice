class MouseTrack extends React.Component {
  state = {
    mousePosition: []
  };
  trackMousePos = e => {
    this.setState({
      mousePosition: [e.clientX, e.clientY]
    });
  };
  componentDidMount() {
    document.addEventListener('mousemove', this.trackMousePos)
  }
  componentWillUnmount() {
    document.removeEventListener(
      'mousemove',
      this.trackMousePos
    )
  }

  render() {
    return (
      <div>
        <h3 className="app__title">Позиция курсора:</h3>
        <h2>
          X: {this.props.trackMouse ? this.state.mousePosition[0] : ' -'}
          <br />
          Y: {this.props.trackMouse ? this.state.mousePosition[1] : ' -'}
        </h2>
      </div>
    );
  }
}

function MouseTrackHook() {
  const [state, setState] = React.useState([]);
  
  const trackMousePos = e => {
    setState([e.clientX, e.clientY]);
  };
  
  React.useEffect(
    ()=> {
          document.addEventListener('mousemove', trackMousePos);
          return () => document.removeEventListener('mousemove', trackMousePos);
         }
  )

     return (
      <div>
        <h3 className="app__title">Позиция курсора:</h3>
        <h2>
          X: {this.props.trackMouse ? this.state.mousePosition[0] : ' -'}
          <br />
          Y: {this.props.trackMouse ? this.state.mousePosition[1] : ' -'}
        </h2>
      </div>
    );
}

