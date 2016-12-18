var React = require("react");

var DescriptionContainer = React.createClass({
	propTypes: {
		desc: React.PropTypes.string,
		profession: React.PropTypes.string
	},
	render: function() {
		return (
			<div style={{width:"63%", height:"50%", marginLeft:"3px", float:"right", position:"relative", position:"relative", top:"15px"}}>
				<div style={{height:"35px", width:"100%", marginTop:"50px", backgroundColor:"#ff6666"}}>
					<h3 style={{paddingTop:"5px", paddingLeft:"5px"}}>Information</h3>
					<div style={{height:"5px", width:"100%", margin:"-7px 0px 0px 0px", backgroundColor:"#ff2222"}}></div>
				</div>
				<div style={{backgroundColor:"#fff", height:"70%"}}>
					<h4 style={{position:"relative", top:"5px", padding:"0px 10px"}}>{this.props.desc}</h4>
					<h4 style={{position:"absolute", bottom:"15px", padding:"0px 10px"}}>{this.props.profession}</h4>
				</div>
			</div>
		);
	}
});

module.exports = DescriptionContainer;