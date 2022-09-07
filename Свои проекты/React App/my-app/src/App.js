import React, { useEffect, useMemo, useRef, useState } from "react";
import ClassCounter from "./components/classCounter";
import Counter from "./components/counter";
import PostFilter from "./components/PostFilter";
import PostForm from "./components/PostForm";
import PostItem from "./components/PostItem";
import PostList from "./components/PostList";
import MyButton from "./components/UI/button/MyButton";
import MyInput from "./components/UI/input/MyInput";
import MyModal from "./components/UI/MyModal/MyModal";
import MySelect from "./components/UI/select/MySelect";
import axios from "axios";
import { usePosts } from "./hooks/usePosts";
import "./styles/App.css";
import PostService from "./API/PostService";
import Loader from "./components/UI/loader/Loader";
import { useFetching } from "./hooks/useFetching";
import { getPageCount, getPagesArray } from "./utils/pages";
import Pagination from "./components/UI/pagination/Pagination";

function App() {
  // let likes = 0;

  // function increment() {
  //   likes += 1;
  //   console.log(likes);
  // }

  // const [likes, setLikes] = useState(69);
  // const [value, setValue] = useState("TEXT OMG");

  const [posts, setPosts] = useState([
    { id: 1, title: "LULE", body: "Эмоут для посмеяться" },
    { id: 2, title: "OMEGALUL", body: "Открыл рот и молчит" },
    { id: 3, title: "kot", body: "КОТ monkaOMEGA" },
  ]);
  const [filter, setFilter] = useState({ sort: "", query: "" });
  const [modal, setModal] = useState(false);
  const sortedAndSearchedPosts = usePosts(posts, filter.sort, filter.query);
  const [totalPages, setTotalPages] = useState(0);
  const [limit, setLimit] = useState(10);
  const [page, setPage] = useState(1);

  const [fetchPosts, isPostsLoading, postError] = useFetching(async (limit, page) => {
    const response = await PostService.getAll(limit, page);
    setPosts(response.data);
    const totalCount = response.headers["x-total-count"];
    setTotalPages(getPageCount(totalCount, limit));
  });

  useEffect(() => {
    fetchPosts(limit, page);
  }, []);

  const changePage = (page) => {
    setPage(page)
    fetchPosts(limit, page)
  }

  const createPost = (newPost) => {
    setPosts([...posts, newPost]);
    setModal(false);
  };

  const removePost = (post) => {
    setPosts(posts.filter((p) => p.id !== post.id));
  };

  return (
    <div className="App">
      <MyButton style={{ marginTop: "15px" }} onClick={() => setModal(true)}>
        Добавить эмоут
      </MyButton>
      <MyModal visible={modal} setVisible={setModal}>
        <PostForm create={createPost} />
      </MyModal>
      <hr style={{ margin: "15px 0px" }} />
      <PostFilter filter={filter} setFilter={setFilter} />
      {postError && <h2>Произошла ошибка: ${postError}</h2>}
      {isPostsLoading ? (
        <div
          style={{ display: "flex", justifyContent: "center", marginTop: 50 }}
        >
          <Loader />
        </div>
      ) : (
        <PostList
          remove={removePost}
          posts={sortedAndSearchedPosts}
          title="monkaOMEGA"
        />
      )}
      <Pagination page={page} totalPages={totalPages} changePage={changePage}/>
    </div>
  );
}

export default App;
