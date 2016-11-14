import $ from 'jquery';  
import React, { Component } from 'react';
import { Link } from 'react-router';

class Tips extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div className="panel panel-default">
                <div className="panel-heading">  
                    { this.props.tipData.title }
                </div>
                <div className="panel-body lead">
                    { this.props.tipData.notes }
                </div>
                <Tricks tricksData={this.props.tipData.tricks} />
            </div>
        );
    }
}

class Tricks extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        var tricks = this.props.tricksData.map(function(row, i) {
                        return (
                            <Trick trickData={row} key={row.id} />
                        );
                    });

        return (
            <div>{ tricks }</div>
        );
    }
}

class Trick extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <li className="list-group-item">
                 <code>{ this.props.trickData.command }</code>
            </li>
        );
    }
}


export default class Section extends Component {

    constructor(props) {
        super(props);
        this.state = {
            data: [],
            intervalId: null            
        };
    }

    loadTipsFromServer(){
        const loadThis = "/api/tipstricks/" + this.props.params.id;

        $.ajax({
            url: loadThis,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
                clearInterval(this.state.intervalId);
            }.bind(this)
        })
    }

    componentDidMount() {
        this.loadTipsFromServer();
        var intervalId = setInterval(this.loadTipsFromServer, 1000);
        this.setState({intervalId: intervalId});
    }

    renderResults(tipsData) {
      return (
        <Tips tipData={tipsData} key={tipsData.id} />
      );
    }

    render() {
        var results = "";
        if(this.state.data.results) {
            if(this.state.data.results.length >0) {
                results = this.state.data.results.map(this.renderResults);
            }
            else {
                results = (
                    <div className="row">
                        <div className="col-md-12 div-padded">
                            There are no tips yet.
                        </div>
                    </div>
                );
            }
        }
        return (
            <div>
                {results}
                <Link to="/tips/" className="btn btn-default">
                  Back
                </Link> 
            </div>
        );
    }
}