import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Chakra, Module, Sass, Styled } from "./pages";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<div>hi</div>} />
        <Route path="/module" element={<Module />} />
        <Route path="/scss" element={<Sass />} />
        <Route path="/styled" element={<Styled />} />
        <Route path="/chakra" element={<Chakra />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
