/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (function() { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./components/main.js":
/*!****************************!*\
  !*** ./components/main.js ***!
  \****************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _main_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./main.scss */ \"./components/main.scss\");\n\n\nfunction colorRatings(item, total_rating) {\n  // Update stars coloring in form\n  var selected_rating = item.charAt(item.length - 1);\n\n  for (var i = 0; i < total_rating; i++) {\n    if (i <= Number(selected_rating)) {\n      document.getElementById('id_review-rating_' + i).classList.add('star-full');\n      document.getElementById('id_review-rating_' + i).classList.remove('star-empty');\n    } else {\n      document.getElementById('id_review-rating_' + i).classList.add('star-empty');\n      document.getElementById('id_review-rating_' + i).classList.remove('star-full');\n    }\n  }\n}\n\ndocument.addEventListener('DOMContentLoaded', function () {\n  // Wait for document to be loaded\n  var rating_inputs = document.querySelectorAll('#rating input[name=\"review-rating\"]');\n\n  if (rating_inputs) {\n    var _loop = function _loop(item) {\n      // Event listener for checked item\n      rating_inputs[item].addEventListener('click', function () {\n        if (rating_inputs[item].checked) {\n          colorRatings(rating_inputs[item].id, rating_inputs.length);\n        }\n      }); // Set initial stars\n\n      if (rating_inputs[item].checked) {\n        colorRatings(rating_inputs[item].id, rating_inputs.length);\n      }\n    };\n\n    for (var item = 0; item < rating_inputs.length; item++) {\n      _loop(item);\n    }\n  }\n}, false);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9jb21wb25lbnRzL21haW4uanMuanMiLCJtYXBwaW5ncyI6Ijs7QUFBQTs7QUFFQTtBQUNBO0FBQ0E7O0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQUE7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBWEE7O0FBQ0E7QUFBQTtBQVdBO0FBQ0E7QUFDQSIsInNvdXJjZXMiOlsid2VicGFjazovL2xpdHJldmlldy8uL2NvbXBvbmVudHMvbWFpbi5qcz9lZmZiIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCAnLi9tYWluLnNjc3MnXHJcblxyXG5mdW5jdGlvbiBjb2xvclJhdGluZ3MoaXRlbSwgdG90YWxfcmF0aW5nKSB7XHJcbiAgLy8gVXBkYXRlIHN0YXJzIGNvbG9yaW5nIGluIGZvcm1cclxuICBsZXQgc2VsZWN0ZWRfcmF0aW5nID0gaXRlbS5jaGFyQXQoaXRlbS5sZW5ndGggLSAxKTtcclxuICBmb3IgKGxldCBpID0gMDsgaSA8IHRvdGFsX3JhdGluZzsgaSsrKSB7XHJcbiAgICBpZiAoaSA8PSBOdW1iZXIoc2VsZWN0ZWRfcmF0aW5nKSkge1xyXG4gICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaWRfcmV2aWV3LXJhdGluZ18nICsgaSkuY2xhc3NMaXN0LmFkZCgnc3Rhci1mdWxsJylcclxuICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2lkX3Jldmlldy1yYXRpbmdfJyArIGkpLmNsYXNzTGlzdC5yZW1vdmUoJ3N0YXItZW1wdHknKVxyXG4gICAgfSBlbHNlIHtcclxuICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2lkX3Jldmlldy1yYXRpbmdfJyArIGkpLmNsYXNzTGlzdC5hZGQoJ3N0YXItZW1wdHknKVxyXG4gICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaWRfcmV2aWV3LXJhdGluZ18nICsgaSkuY2xhc3NMaXN0LnJlbW92ZSgnc3Rhci1mdWxsJylcclxuICAgIH1cclxuICB9XHJcbn1cclxuXHJcbmRvY3VtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ0RPTUNvbnRlbnRMb2FkZWQnLCBmdW5jdGlvbiAoKSB7XHJcbiAgLy8gV2FpdCBmb3IgZG9jdW1lbnQgdG8gYmUgbG9hZGVkXHJcbiAgbGV0IHJhdGluZ19pbnB1dHMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKFxyXG4gICAgJyNyYXRpbmcgaW5wdXRbbmFtZT1cInJldmlldy1yYXRpbmdcIl0nKTtcclxuICBpZiAocmF0aW5nX2lucHV0cykge1xyXG4gICAgZm9yIChsZXQgaXRlbSA9IDA7IGl0ZW0gPCByYXRpbmdfaW5wdXRzLmxlbmd0aDsgaXRlbSsrKSB7XHJcbiAgICAgIC8vIEV2ZW50IGxpc3RlbmVyIGZvciBjaGVja2VkIGl0ZW1cclxuICAgICAgcmF0aW5nX2lucHV0c1tpdGVtXS5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIGZ1bmN0aW9uICgpIHtcclxuICAgICAgICBpZiAocmF0aW5nX2lucHV0c1tpdGVtXS5jaGVja2VkKSB7XHJcbiAgICAgICAgICBjb2xvclJhdGluZ3MocmF0aW5nX2lucHV0c1tpdGVtXS5pZCwgcmF0aW5nX2lucHV0cy5sZW5ndGgpO1xyXG4gICAgICAgIH1cclxuICAgICAgfSlcclxuICAgICAgLy8gU2V0IGluaXRpYWwgc3RhcnNcclxuICAgICAgaWYgKHJhdGluZ19pbnB1dHNbaXRlbV0uY2hlY2tlZCkge1xyXG4gICAgICAgIGNvbG9yUmF0aW5ncyhyYXRpbmdfaW5wdXRzW2l0ZW1dLmlkLCByYXRpbmdfaW5wdXRzLmxlbmd0aCk7XHJcbiAgICAgIH1cclxuICAgIH1cclxuICB9XHJcbn0sIGZhbHNlKTsiXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./components/main.js\n");

/***/ }),

/***/ "./components/main.scss":
/*!******************************!*\
  !*** ./components/main.scss ***!
  \******************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9jb21wb25lbnRzL21haW4uc2Nzcy5qcyIsIm1hcHBpbmdzIjoiO0FBQUEiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9saXRyZXZpZXcvLi9jb21wb25lbnRzL21haW4uc2Nzcz83NmI4Il0sInNvdXJjZXNDb250ZW50IjpbIi8vIGV4dHJhY3RlZCBieSBtaW5pLWNzcy1leHRyYWN0LXBsdWdpblxuZXhwb3J0IHt9OyJdLCJuYW1lcyI6W10sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./components/main.scss\n");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	!function() {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = function(exports) {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	}();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval-source-map devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./components/main.js");
/******/ 	
/******/ })()
;