var React = require("react");

var NewsContainer = React.createClass({
	propTypes: {
		article: React.PropTypes.array.isRequired
	},
	render: function() {
		return (
			<div style={{float:"left", width:"99%", height:"93%", marginLeft:"4px", marginTop:"4px", overflow:"auto"}}>
				{this.props.articles.map(function(article, index) {
					return (
						<div key={index} style={{backgroundColor:"#ffffff" ,border:"5px solid #ff6666", float:"left", width:"32%", height:"95%", marginLeft:"4px", marginTop:"4px", overflow:"auto", display:"inline-block"}}>
							<p style={{textAlign:"center", marginLeft:"10px", marginRight:"10px"}}><b><a href={article.url} target="_blank">{article.articleName}</a></b></p>
							<img src={article.articleImage} alt="article photo" style={{width:"95%", margin:"auto", display:"block"}}/>
							<p style={{textAlign:"center", marginLeft:"5px", marginRight:"5px"}}>{article.articleDescription}</p>
						</div>
					)
				})}
			</div>
		)
	}
});

module.exports = NewsContainer;