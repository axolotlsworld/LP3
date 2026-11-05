// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint) balanceOf;

    function deposit() public payable {
        require(msg.value > 0, "Deposit should be greater than zero.");
        balanceOf[msg.sender] += msg.value;
    }

    function withdraw() public {
        require(balanceOf[msg.sender] > 0, "Your balance should be greater than zero.");
        payable(msg.sender).transfer(balanceOf[msg.sender]);
        balanceOf[msg.sender] = 0;
    }

    function showBalance() public view returns(uint) {
        return balanceOf[msg.sender];
    }
}
