from dataclasses import asdict

import pytest
from sqlalchemy import select

from fast_zero.models import User


@pytest.mark.asyncio
async def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username='testuser',
            password='password123',
            email='teste@teste.com',
        )
        session.add(new_user)
        await session.commit()
    user = await session.scalar(
        select(User).where(User.username == 'testuser')
    )
    assert asdict(user) == {
        'id': 1,
        'username': 'testuser',
        'password': 'password123',
        'email': 'teste@teste.com',
        'created_at': time,
    }
