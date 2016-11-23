import $ from 'jquery';  
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Router, Route, Link, IndexRoute, browserHistory } from 'react-router';
import Section from './section';

export default class SectionList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            data: []          
        };
    }

    loadSectionsFromServer(){
        $.ajax({
            url: '/api/sections/',
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    }

    componentDidMount() {
        this.loadSectionsFromServer();
    } 

    render() {
        if (this.state.data.results) {
            var sectionNodes = this.state.data.results.map(function(section){
                return (
                    <div className="row" key={section.id}>
                        <div className="col-md-4 div-padded"> 
                            <Link to={`/tips/section/${section.id}`} className="btn btn-primary btn-lg btn-block outline">
                                {section.title}
                            </Link>
                        </div>
                    </div>
                );
            }, this)
        }
        return (
            <div>
                {this.props.children ? this.props.children : sectionNodes}
            </div>
        )
    }
}

ReactDOM.render((
  <Router history={browserHistory}>
    <Route path="/tips/" component={SectionList} >
        <Route path="section/:id" component={Section} />
    </Route>
  </Router>
), document.getElementById('container'))