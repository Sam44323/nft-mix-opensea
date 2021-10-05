// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    uint256 public tokenCounter;

    constructor() public ERC721("Dogie", "DOG") {}

    function createCollectible() public returns (uint256) {
        uint256 newTokenId = tokenCounter;
        _safeMint(msg.sender, newTokenId); // minting a new nft with the owner address and the token-id for it
        tokenCounter += 1;
        return newTokenId;
    }
}
