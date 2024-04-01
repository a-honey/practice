import styled from "styled-components";

const Styled = () => {
  return (
    <main>
      <h2>Styled 페이지</h2>
      <Container>
        <h2>컨테이너아이템</h2>
        <h2>컨테이너아이템</h2>
        <h2>컨테이너아이템</h2>
      </Container>
    </main>
  );
};

export default Styled;
const Container = styled.section`
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: pink;
`;
