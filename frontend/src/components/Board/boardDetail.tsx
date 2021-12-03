import React from 'react';
import BoardColumns from "./boardColumns";

type Props = {
    boardId: number;
};


const BoardDetail: React.FC<Props> = ({boardId} ) => {

    return (
        <div><BoardColumns boardId={boardId}>

        </BoardColumns></div>
    );
};

export default BoardDetail;
