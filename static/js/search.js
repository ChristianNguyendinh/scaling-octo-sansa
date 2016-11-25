var React = require("react");
var ReactDOM = require("react-dom");
var $ = require("jquery");

var PlaceHolder = React.createClass({
	getInitialState: function() {
		return {text: ""};
	},
	handleSubmit: function(e) {
		e.preventDefault();
		// replace space between words,
		var fstr = this.state.text.trim().replace(" ", "-").replace(/ /g, "");
		var url = "http://127.0.0.1:8000/search/info/" + fstr;
		//console.log(url);
		//if (/^[a-z- ]+$/i.test(fstr))
		window.location = url
	},
	handleChange: function(e) {
		this.setState({text: e.target.value});
	},
	render: function() {
		return (
			<div style={{width:"100%", height:"100%", position:"relative"}}>
				<div style={{width:"300px", height:"200px", position:"absolute", top:"30%", right:"40%"}}>
					<h1 style={{color:"#000"}}>Enter a name to search: </h1>
					<form onSubmit={this.handleSubmit}>
						<input type="text" value={this.state.text} onChange={this.handleChange} pattern="[A-Za-z- ]+" required/>
						<br/>
						<input type="submit" value="search"/>
						<p></p>
					</form>
				</div>
			</div>
		);
	}
});

ReactDOM.render(<PlaceHolder />, document.getElementById('content'));