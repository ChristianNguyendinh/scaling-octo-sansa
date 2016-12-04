var React = require("react");

var TwitterContainer = React.createClass({
	propTypes: {
		urls: React.PropTypes.array.isRequired
	},
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

module.exports = TwitterContainer;