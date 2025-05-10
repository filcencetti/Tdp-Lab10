import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        if int(self._view._txtAnno.value) not in [v for v in range(1861,2016)]:
            self._view.create_alert("L'anno inserito non è valido")
            self._view._txtAnno.value = ""
            self._view.update_page()
            return

        self._model.buildGraph(self._view._txtAnno.value)
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {len(self._model._graph.nodes())} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))


        for country in sorted(self._model._graph.nodes(),key=lambda x:x.StateName):
            self._view._txt_result.controls.append(ft.Text(f"{country} -- {self._model._graph.degree(country)} vicini"))

        self._view.update_page()

    def handleReachableCountries(self, e):
        self._view._txt_result.controls.clear()
        self._model.getReachableState(self._state)
        for country in self._model._reachableCountries:
            if country != self._state:
                self._view._txt_result.controls.append(ft.Text(country))
        self._view.update_page()

    def fillCountries(self,year):
        for c in self._model._countries:
            self._view._ddCountries.options.append(ft.dropdown.Option(text=c.StateName, data=c,on_click=self.read_country))
        self._view.update_page()

    def read_country(self,e):
        self._state = e.control.data