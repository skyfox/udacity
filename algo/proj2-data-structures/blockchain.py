from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Text, Optional


class Block:
    """A blockchain block."""

    def __init__(self, data: Text, previous_block: Optional[Block] = None) -> None:
        """Class constructor.

        We don't want a user of the class to give a direct access to some class properties.
        Hence almost all of them are private and available only via getters.

        Args:
            data: block's text.
            previous_block: the hash value of a previous block.
        """
        self._data = data
        self._previous_block = previous_block
        self._previous_hash = previous_block._hash if previous_block else None
        self._hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
        self._timestamp = datetime.now(tz=timezone.utc)

    @property
    def hash(self) -> str:
        """Returns the hash of a block."""
        return self._hash

    @property
    def prev_hash(self) -> str:
        """Returns the hash of the previous block."""
        return self._previous_hash

    @property
    def timestamp(self) -> str:
        """Returns the timestamp of a block."""
        return self._timestamp

    @property
    def previous_block(self):
        return self._previous_block

    @previous_block.setter
    def previous_block(self, block: Block):
        self._previous_block = block
        self._previous_hash = block.hash

    def __repr__(self):
        """Represents the block as a string."""
        return "Block[timestamp={ts}, data={data}]".format(ts=self._timestamp, hs=self._hash, data=self._data)


class Blockchain:
    """A blockchain."""

    def __init__(self) -> None:
        self._tail = None

    def append(self, block: Block) -> None:
        """Append a new block to a blockchain.

        Args:
            block: a block to append.
        """
        if self._tail:
            block.previous_block = self._tail
            self._tail = block
        else:
            self._tail = block

    @property
    def tail(self) -> Optional[Block]:
        """Returns a tail."""
        return self._tail

    def __repr__(self) -> str:
        """Represents the chain as a string with arrows."""
        out = "void"
        block = self._tail
        while block:
            out = out + " <- " + self._tail.__repr__()
            block = block.previous_block
        return out


if __name__ == "__main__":
    bc = Blockchain()
    b1 = Block("First Block")
    b2 = Block("Second Block")
    b3 = Block("Third block")
    bc.append(b1)
    bc.append(b2)
    bc.append(b3)
    assert b1.hash == b2.prev_hash
    print(bc)
