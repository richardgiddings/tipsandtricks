'use strict';

var $ = require('jquery');  
var React = require('react')
var ReactDOM = require('react-dom')

var SectionList = React.createClass({
    loadSectionsFromServer: function(){
        $.ajax({
            url: this.props.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this)
        })
    },

    getInitialState: function() {
        return {data: []};
    },

    componentDidMount: function() {
        this.loadSectionsFromServer();
        setInterval(this.loadSectionsFromServer, 
                    this.props.pollInterval)
    }, 


    handleClick: function(section_id, event) {
        this.setState({section: section_id});
    },

    render: function() {
        if (this.state.data.results) {
            var sectionNodes = this.state.data.results.map(function(section){
                return (
                    <div className="row" key={section.id}>
                        <div className="col-md-4 div-padded"> 
                            <a className="btn btn-primary btn-lg btn-block outline" onClick={this.handleClick.bind(this, section.id)} href={`${section.id}/section/`}>
                                {section.title}
                            </a>
                        </div>
                    </div>
                );
            }, this)
        }
        return (
            <div>
                {sectionNodes}
            </div>
        )
    }
})

ReactDOM.render(<SectionList url='/api/sections/' pollInterval={1000} />, 
    document.getElementById('container'))