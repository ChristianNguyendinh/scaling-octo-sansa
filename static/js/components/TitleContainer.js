var React = require("react");

var TitleContainer = React.createClass({
	propTypes: {
		name: React.PropTypes.string.isRequired,
		image: React.PropTypes.string.isRequired
	},
	render: function() {
		return (
			<div style={{width:"35%", height:"50%", float:"left", overflow:"hidden"}}>
				<div>
					<div style={{width:"100%", marginTop:"15px", marginBottom:"15px"}}>
						<div className="testme" style={{width:"250px", marginLeft:"12px", height:"5px", backgroundColor:"blue"}}></div>
						<h2 style={{margin:"2px 2px 2px 15px"}}>{this.props.name}</h2>
						<div className="testme" style={{width:"250px", marginLeft:"12px", height:"5px", backgroundColor:"blue"}}></div>
					</div>
					<img src={this.props.image} width="275px" style={{marginLeft:"5px"}}/>
				</div>
			</div>
		);
	}
});

module.exports = TitleContainer;