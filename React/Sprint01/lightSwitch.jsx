function Switch() {
  const [isActive, switchLight] = React.useState(false)
  
  handleClick = () => {
    switchLight(!isActive)
  }

  const className = `root ${isActive ? 'on' : 'off'}`;

  return (
    <div className={className}>
      <div className={'sideWall'}>
        <button className={'button'} onClick={handleClick}/>
      </div>
      <div className={'catWrap'}>
        <div className={'bubble'}/>
        <div className={'wall'}/>
        <div className={'floor'}/>
        <div className={'cat'}/>
      </div>
    </div>
  );
}

ReactDOM.render(<Switch />, document.querySelector('#root'));
