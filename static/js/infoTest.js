// file is only for testing, for real thing, put componenets in folder and use webpack to bundle

var TwitterContainer = React.createClass({
	render: function() {
		return (
			<div style={{color:"blue", width:"38%", height:"100%", marginLeft:"5px", float:"right"}}>
				<h3>Most Recent Tweets</h3>
				{this.props.urls.map(function(url) {
					return (
						<div>
							<blockquote data-cards="hidden" className="twitter-tweet" width="550">
								<a href={"https://twitter.com/" + url}>pce</a>
							</blockquote>
						</div>
					)
				})}
			</div>
		);
	}
});

var DescriptionContainer = React.createClass({
	render: function() {
		return (
			<div style={{color:"green", width:"63%", height:"50%", marginLeft:"3px", float:"right"}}>
				<h3>{this.props.desc}</h3>
			</div>
		);
	}
});

var TitleContainer = React.createClass({
	render: function() {
		return (
			<div style={{color:"yellow", width:"35%", height:"50%", float:"left", overflow:"hidden"}}>
				<div>
					<h3>{this.props.name}</h3>
					<img src={this.props.image} width="275px"/>
				</div>
			</div>
		);
	}
});

var InfoContainer = React.createClass({
	getInitialState: function() {
		return {data: [], listUrls: []};
	},
	getData: function() {
		console.log('polling');
		$.ajax({
			url: "http://127.0.0.1:8000/search/api/" + document.getElementById('themaineone').innerHTML + ".json",
			dataType: 'json',
			cache: false,
			success: function(data) {
				this.setState({data: data});
				this.setState({listUrls: [data.urls1, data.urls2, data.urls3]});
				//limited to 3 out of the 5 for now
			}.bind(this),
			error: function(xhr, status, err) {
				console.error("http://127.0.0.1:8000/search/api/taylor-swift.json", status, err.toString());
			}.bind(this)
		});
	},
	componentDidMount: function() {
		this.getData();
	},
	componentDidUpdate: function() {
		window.twttr.widgets.load();
	},
	render: function() {
		var listUrls = [];
		return (
			<div id="container">
				<div id="leftContainer">
					<TitleContainer name={this.state.data.name} image={this.state.data.image}/>
					<DescriptionContainer desc={this.state.data.description}/>
					<div style={{border:"2px solid red", clear:"both", width:"100%", height:"45%"}}>
						<div style={{border:"2px solid purple", float:"left", width:"33%", height:"95%", marginLeft:"4px", marginTop:"4px"}}>
							<p>Graphs & Charts</p>
						</div>
						<div style={{border:"2px solid orange", float:"right", width:"65%", height:"95%", marginRight:"4px", marginTop:"4px"}}>
							<p>News API</p>
						</div>
					</div>
				</div>
				<TwitterContainer urls={this.state.listUrls}/>
			</div>
		);
	}
});
ReactDOM.render(<InfoContainer />, document.getElementById('content'));


