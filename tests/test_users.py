import pytest

class TestUserCreation:

    def test_create_user_all_fields_valid(self, client):
        """Test sa svim validnim poljima"""
        data = {
            'email': 'complete@test.com', 
            'username': 'completeuser', 
            'password': 'Complete123'}


        response = client.post('/api/users/', json=data)
        assert response.status_code == 201
        user = response.json()
        assert user['email']==data['email']
        assert user['username']==data['username']
        assert 'id' in user
        assert 'created_at' in user
        assert 'password' not in user
        assert 'hashed_password' not in user

    def test_create_user_succes(self, client):

        data = {
            'email' : 'test@example.com', 
            'username' : 'testuser', 
            'password' : 'TestPass123'}

        response = client.post('/api/users/', json = data)
        assert response.status_code == 201
        assert response.json()['email']=='test@example.com'

    def test_create_user_duplicate_email(self, client):
        """Test kreiranje korisnika sa email koji vec postoji"""
        first_user = {
            'email': 'isti@example.com', 
            'username':'prviuser', 
            'password': 'Prvalozonka123!'}

        response1 = client.post ('/api/users/', json = first_user)
        assert response1.status_code == 201

        second_user = {
            'email': 'isti@example.com', 
            'username': 'drugiuser', 
            'password': 'DrugaLozinka123!'}

        response2 = client.post('/api/users/', json =second_user)
        assert response2.status_code == 409
        error = response2.json()
        assert 'detail' in response2.json()
        assert 'already registered' in response2.json()['detail'].lower()



