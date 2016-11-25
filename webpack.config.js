module.exports = {
	entry: {
		search: __dirname + '/static/js/search.js',
		info: __dirname + '/static/js/infoTest.js'
	},
	module: {
		loaders: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loader: 'babel-loader',
				query: {
					presets:['react']
				}
			}
		]
	},
	output: {
		filename: 'transformed_[name].js',
		path: __dirname + '/static/build/js'
	},
};