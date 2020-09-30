class Scene(object):

    map = {
        'lobby_room': LobbyRoom(),
        'weapon_room': WeaponRoom(),
        'koi_pond_room': KoiPondRoom(),
        'boss_room': BossRoom(),
        'vault_room': VaultRoom()
    }
    def __init__(self):
        self.next_scene = None
        rum = VaultRoom()
        rum.enter()


class LobbyRoom(Scene):

    def enter(self):
        pass


class WeaponRoom(Scene):

    def enter(self):
        pass


class KoiPondRoom(Scene):

    def enter(self):
        pass


class BossRoom(Scene):

    def enter(self):
        pass


class VaultRoom(Scene):

    def enter(self):
        print('It works')
        pass
