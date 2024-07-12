import React from 'react';

const Header = () => {
    const title = "Pokémon Duel Simulator";
    const slogan = "Become a Pokémon Master!";

    return (
        <header>
            <h1>{title}</h1>
            <p>{slogan}</p>
        </header>
    );
};

export default Header;