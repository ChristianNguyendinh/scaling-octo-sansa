var React = require("react");
var ReactDOM = require("react-dom");

var NewsContainer = require("./components/NewsContainer.js");
var TitleContainer = require("./components/TitleContainer.js");
var TwitterContainer = require("./components/TwitterContainer.js");
var DescriptionContainer = require("./components/DescriptionContainer.js");

var $ = require("jquery");

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
			})
		).then(function() {
			$.ajax({
				url: "http://127.0.0.1:8000/search/api/articles/" + document.getElementById('themaineone').innerHTML + ".json",
				dataType: 'json',
				cache: false,
				success: function(data) {
					//alert("loaded articles")
					articles = data;
					this.setState({data: dataList, listUrls: urls, articleList: articles});
				}.bind(this),
				error: function(xhr, status, err) {
					console.error("http://127.0.0.1:8000/search/api/taylor-swift.json", status, err.toString());
				}.bind(this)
			})

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
					<div style={{clear:"both", width:"100%", height:"45%"}}>
						<h3 style={{margin:"0px 10px"}}>News</h3>
						<NewsContainer articles={this.state.articleList}/>
					</div>
				</div>
				<TwitterContainer urls={this.state.listUrls}/>
			</div>
		);
	}
});

ReactDOM.render(<InfoContainer />, document.getElementById('content'));


