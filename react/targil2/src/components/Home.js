import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import Pokeball from "./../pokeball.png";

class Home extends Component {
  state = {
    posts: [],
  };
  render() {
    const { posts } = this.state;
    const postList = posts.length ? (
      posts.map((post) => {
        return (
          <div className="post card" key={post.id}>
            <img src={Pokeball} alt="a pokeball" />
            <div className="card-content">
              <span className="card-title">{post.title}</span>
            </div>
            <div className="card-action">
              <Link to={`/posts/${post.id}`}>
                <span>view</span>
              </Link>
            </div>
          </div>
        );
      })
    ) : (
      <div className="center">No posts to show</div>
    );
    return (
      <div className="container">
        <h4 className="center">Home</h4>
        {postList}
      </div>
    );
  }
  componentDidMount() {
    axios.get("https://jsonplaceholder.typicode.com/posts").then((res) => {
      console.log(res);
      this.setState({
        posts: res.data.slice(0, 10),
      });
    });
  }
}

export default Home;
