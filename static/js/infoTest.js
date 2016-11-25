var React = require("react");
var ReactDOM = require("react-dom");
var $ = require("jquery");

// file is only for testing, for real thing, put componenets in folder and use webpack to bundle

var NewsContainer = React.createClass({
	render: function() {
		return (
			<div style={{border:"2px solid orange", float:"left", width:"99%", height:"93%", marginLeft:"4px", marginTop:"4px", overflow:"auto"}}>
				{this.props.articles.map(function(article, index) {
					return (
						<div key={index} style={{border:"2px solid black", float:"left", width:"32%", height:"95%", marginLeft:"4px", marginTop:"4px", overflow:"auto", display:"inline-block"}}>
							<p style={{textAlign:"center"}}>{article.articleName}</p>
							<img src={article.articleImage} alt="article photo" width="150" style={{margin:"auto", display:"block"}}/>
							<p style={{textAlign:"center", marginLeft:"5px", marginRight:"5px"}}>{article.articleDescription}</p>
						</div>
					)
				})}
			</div>
		)
	}
});

var TwitterContainer = React.createClass({
	render: function() {
		return (
			<div style={{color:"blue", width:"38%", height:"100%", marginLeft:"5px", float:"right"}}>
				<h3>Most Recent Tweets</h3>
				{this.props.urls.map(function(url, index) {
					return (
						<div key={index}>
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
			<div style={{color:"green", width:"63%", height:"50%", marginLeft:"3px", float:"right", position:"relative"}}>
				<h3 style={{position:"absolute", top:"45px"}}>{this.props.desc}</h3>
				<h3 style={{position:"absolute", bottom:"15px"}}>{this.props.profession}</h3>
			</div>
		);
	}
});

var TitleContainer = React.createClass({
	render: function() {
		return (
			<div style={{color:"yellow", width:"35%", height:"50%", float:"left", overflow:"hidden"}}>
				<div>
					<h2 style={{marginTop:"15px", marginBottom:"15px"}}>{this.props.name}</h2>
					<img src={this.props.image} width="275px"/>
				</div>
			</div>
		);
	}
});

var InfoContainer = React.createClass({
	getInitialState: function() {
		return {data: [], listUrls: [], articleList: []};
	},
	getData: function() {
		console.log('polling');
		var dataList = [];
		var urls = [];
		var articles = [];
		$.when(
			$.ajax({
				url: "http://127.0.0.1:8000/search/api/" + document.getElementById('themaineone').innerHTML + ".json",
				dataType: 'json',
				cache: false,
				success: function(data) {
					//this.setState({data: data});
					//this.setState({listUrls: [data.urls1, data.urls2, data.urls3]});
					dataList = data;
					urls = [data.urls1, data.urls2, data.urls3];
					//limited to 3 out of the 5 for now
				}.bind(this),
				error: function(xhr, status, err) {
					console.error("http://127.0.0.1:8000/search/api/taylor-swift.json", status, err.toString());
				}.bind(this)
			}),
			$.ajax({
				url: "http://127.0.0.1:8000/search/api/articles/" + document.getElementById('themaineone').innerHTML + ".json",
				dataType: 'json',
				cache: false,
				success: function(data) {
					articles = data;
				}.bind(this),
				error: function(xhr, status, err) {
					console.error("http://127.0.0.1:8000/search/api/taylor-swift.json", status, err.toString());
				}.bind(this)
			}),
		).then(function() {
			this.setState({data: dataList, listUrls: urls, articleList: articles});
			console.log(this.state.articleList);
		}.bind(this));
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
					<DescriptionContainer desc={this.state.data.description} profession={this.state.data.profession}/>
					<div style={{border:"2px solid red", clear:"both", width:"100%", height:"45%"}}>
						<p style={{margin:"0px"}}>News</p>
						<NewsContainer articles={this.state.articleList}/>
					</div>
				</div>
				<TwitterContainer urls={this.state.listUrls}/>
			</div>
		);
	}
});
ReactDOM.render(<InfoContainer />, document.getElementById('content'));


