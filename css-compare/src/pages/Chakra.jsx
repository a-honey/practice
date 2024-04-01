import { ChakraProvider } from "@chakra-ui/react";
import { Flex } from "@chakra-ui/react";

const Chakra = () => {
  return (
    <ChakraProvider>
      <main>
        <h2>Chakra 페이지</h2>
        <Flex direction="column">
          <h2>컨테이너아이템</h2>
          <h2>컨테이너아이템</h2>
          <h2>컨테이너아이템</h2>
        </Flex>
      </main>
    </ChakraProvider>
  );
};

export default Chakra;
