const { override } = require('customize-cra');
const addLessLoader = require('customize-cra-less-loader');

module.exports = override(
  addLessLoader({
    lessLoaderOptions: {
      lessOptions: {
        modifyVars: {
          'primary-color': '#398D78',
          'link-color': '#fff',
          'border-radius-base': '2px',
          },
        javascriptEnabled: true,
      },
    },
  }),
);