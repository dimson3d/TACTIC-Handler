from lib.side.Qt import QtWidgets as QtGui
from lib.side.Qt import QtCore

import lib.ui_classes.ui_misc_classes as ui_misc_classes
import lib.ui.checkin_out.ui_commit_queue as ui_commit_queue

import lib.tactic_classes as tc
import lib.global_functions as gf
from lib.environment import env_inst, env_mode


class deleteSobjectWidget(QtGui.QWidget):
    def __init__(self, sobject, parent=None):
        super(self.__class__, self).__init__(parent=parent)

        self.sobject = sobject
        self.shown = False

    def create_ui(self):
        self.shown = True
        self.create_main_layout()
        self.create_checkboxes_widget()
        self.create_files_dependencies_widget()
        self.create_snapshots_dependencies_widget()
        self.create_tasks_dependencies_widget()
        self.create_notes_dependencies_widget()

        self.controls_actions()

    def get_data_dict(self):

        data_dict = {
            'del_files': self.delete_files_checkbox.isChecked(),
            'del_snapshots': self.delete_snapshot_checkbox.isChecked(),
            'del_tasks': self.delete_tasks_checkbox.isChecked(),
            'del_notes': self.delete_notes_checkbox.isChecked(),
        }

        return data_dict

    def showEvent(self, event):
        if not self.shown:
            self.create_ui()

    def controls_actions(self):
        pass

    def create_main_layout(self):
        self.main_layout = QtGui.QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def create_checkboxes_widget(self):
        self.delete_files_checkbox = QtGui.QCheckBox('Delete files')
        self.delete_files_checkbox.setChecked(True)
        self.main_layout.addWidget(self.delete_files_checkbox)

        self.delete_snapshot_checkbox = QtGui.QCheckBox('Delete snapshots')
        self.delete_snapshot_checkbox.setChecked(True)
        self.main_layout.addWidget(self.delete_snapshot_checkbox)

        self.delete_tasks_checkbox = QtGui.QCheckBox('Delete tasks')
        self.delete_tasks_checkbox.setChecked(True)
        self.main_layout.addWidget(self.delete_tasks_checkbox)

        self.delete_notes_checkbox = QtGui.QCheckBox('Delete notes')
        self.delete_notes_checkbox.setChecked(True)
        self.main_layout.addWidget(self.delete_notes_checkbox)

    def create_files_dependencies_widget(self):

        collapse_wdg_files = ui_misc_classes.Ui_collapsableWidget(state=True)
        layout_files = QtGui.QVBoxLayout()
        collapse_wdg_files.setLayout(layout_files)
        collapse_wdg_files.setText('Hide Files Dependencies')
        collapse_wdg_files.setCollapsedText('Show Files Dependencies')

        self.files_tree_widget = QtGui.QTreeWidget()

        layout_files.addWidget(self.files_tree_widget)

        self.main_layout.addWidget(collapse_wdg_files)

    def create_snapshots_dependencies_widget(self):

        collapse_wdg_snapshots = ui_misc_classes.Ui_collapsableWidget(state=True)
        layout_files = QtGui.QVBoxLayout()
        collapse_wdg_snapshots.setLayout(layout_files)
        collapse_wdg_snapshots.setText('Hide Snapshots Dependencies')
        collapse_wdg_snapshots.setCollapsedText('Show Snapshots Dependencies')

        self.files_tree_widget = QtGui.QTreeWidget()

        layout_files.addWidget(self.files_tree_widget)

        self.main_layout.addWidget(collapse_wdg_snapshots)

    def create_tasks_dependencies_widget(self):

        collapse_wdg_tasks = ui_misc_classes.Ui_collapsableWidget(state=True)
        layout_files = QtGui.QVBoxLayout()
        collapse_wdg_tasks.setLayout(layout_files)
        collapse_wdg_tasks.setText('Hide Tasks Dependencies')
        collapse_wdg_tasks.setCollapsedText('Show Tasks Dependencies')

        self.files_tree_widget = QtGui.QTreeWidget()

        layout_files.addWidget(self.files_tree_widget)

        self.main_layout.addWidget(collapse_wdg_tasks)

    def create_notes_dependencies_widget(self):

        collapse_wdg_notes = ui_misc_classes.Ui_collapsableWidget(state=True)
        layout_files = QtGui.QVBoxLayout()
        collapse_wdg_notes.setLayout(layout_files)
        collapse_wdg_notes.setText('Hide Notes Dependencies')
        collapse_wdg_notes.setCollapsedText('Show Notes Dependencies')

        self.files_tree_widget = QtGui.QTreeWidget()

        layout_files.addWidget(self.files_tree_widget)

        self.main_layout.addWidget(collapse_wdg_notes)


class commitWidget(QtGui.QWidget):
    def __init__(self, args_dict, parent=None):
        super(self.__class__, self).__init__(parent=parent)

        self.args_dict = args_dict

        self.item_widget = self.args_dict['item_widget']
        self.commit_item = None
        self.repo = self.args_dict['repo_name']
        self.context = self.args_dict['context']
        self.update_versionless = self.args_dict['update_versionless']
        self.description = self.args_dict['description']
        self.virtual_snapshot = None
        self.shown = False

    def create_ui(self):

        self.shown = True
        self.create_main_layout()
        self.create_info_label_widget()
        self.create_label_widget()
        self.create_checkboxes_widget()
        self.create_versionless_widget()
        self.create_versions_widget()
        self.get_virtual_snapshot()

        self.create_description_widget()

        self.create_edits_widgets()

        self.main_layout.setRowStretch(6, 1)

        self.switch_versionless_label()

        self.controls_actions()

    def get_data_dict(self):

        data_dict = {
            'description': self.description_widget.get_description('plain'),
            'update_versionless': self.update_versionless_checkbox.isChecked(),
            'virtual_snapshot': self.virtual_snapshot,
        }

        return data_dict

    def showEvent(self, event):
        if not self.shown:
            self.create_ui()

    def checkin_progress(self, progress, info_dict):
        self.commit_item.set_progress_indicator_on()
        self.commit_item.set_progress_status(progress, info_dict)

    def commit(self):
        # TODO here will be checkin variants 'upload, etc'
        if not self.commit_item.is_commit_finished():
            print self.args_dict['checkin_app']
            self.update_virtual_snapshot()

    def inplace_chekin(self):

        if self.args_dict['checkin_app'] == 'standalone':
            def inplace_checkin_agent():
                # for in-place checkin
                check_ok = tc.inplace_checkin(
                    self.args_dict['file_paths'],
                    self.virtual_snapshot,
                    self.args_dict['repo_name'],
                    self.args_dict['update_versionless'],
                    self.args_dict['create_icon'],
                    self.args_dict['files_objects'],
                    self.args_dict['padding'],
                    progress_callback=inplace_checkin_worker.emit_progress,
                )
                return check_ok

            inplace_checkin_worker = gf.get_thread_worker(
                inplace_checkin_agent,
                thread_pool=env_inst.get_thread_pool('commit_queue/server_thread_pool'),
                result_func=self.inplace_checkin_done,
                finished_func=self.chekin_snapshot,
                progress_func=self.checkin_progress,
                error_func=gf.error_handle
            )
            inplace_checkin_worker.start()

        if self.args_dict['checkin_app'] == 'maya':
            import lib.maya_functions as mf

            mf.set_info_to_scene(self.args_dict['search_key'], self.args_dict['context'])
            print 'checkin from maya'
            # for in-place checkin
            check_ok, files_objects = mf.inplace_checkin(
                self.virtual_snapshot,
                self.args_dict['repo_name'],
                self.args_dict['update_versionless'],
                self.args_dict['create_icon'],
                selected_objects=self.args_dict['selected_objects'],
                ext_type=self.args_dict['ext_type'],
                setting_workspace=self.args_dict['setting_workspace'],
            )
            print check_ok, files_objects
            if check_ok:
                self.args_dict['files_objects'] = files_objects
                self.chekin_snapshot()

    def inplace_checkin_done(self, result):
        print result

    def chekin_snapshot(self):
        # print self.args_dict
        data_dict = self.get_data_dict()

        def inplace_checkin_agent():
            return tc.checkin_snapshot(
                search_key=self.args_dict['search_key'],
                context=self.args_dict['context'],
                snapshot_type=self.args_dict['snapshot_type'],
                is_revision=self.args_dict['is_revision'],
                description=data_dict['description'],
                version=self.args_dict['version'],
                update_versionless=data_dict['update_versionless'],
                keep_file_name=self.args_dict['keep_file_name'],
                repo_name=self.args_dict['repo_name'],
                virtual_snapshot=data_dict['virtual_snapshot'],
                files_dict=self.args_dict['files_dict'],
                mode=self.args_dict['mode'],
                create_icon=self.args_dict['create_icon'],
                files_objects=self.args_dict['files_objects'],
            )

        snapshot_checkin_worker = gf.get_thread_worker(
            inplace_checkin_agent,
            thread_pool=env_inst.get_thread_pool('commit_queue/server_thread_pool'),
            result_func=self.checkin_done,
            # progress_func=self.checkin_progress,
            error_func=gf.error_handle
        )
        snapshot_checkin_worker.start()

    def checkin_done(self, result):

        self.commit_item.set_commit_finished()

        project_code = tc.split_search_key(self.args_dict['search_key'])
        commit_queue_ui = env_inst.get_commit_queue(project_code['project_code'])
        commit_queue_ui.commit_queue()
        commit_queue_ui.clear_queue_after_checkin()

    def add_commit_item(self, commit_item):
        self.commit_item = commit_item

    def refresh_commit_item_description(self):

        if self.commit_item:
            self.commit_item.set_description(self.description_widget.get_description('plain'))

    def controls_actions(self):
        self.update_versionless_checkbox.stateChanged.connect(self.switch_versionless_label)
        self.description_widget.descriptionTextEdit.textChanged.connect(self.refresh_commit_item_description)

    def create_main_layout(self):
        self.main_layout = QtGui.QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def create_checkboxes_widget(self):
        self.update_versionless_checkbox = QtGui.QCheckBox('Update Versionless')
        self.only_versionless_checkbox = QtGui.QCheckBox('Commit Versionless Only')
        if self.update_versionless:
            self.update_versionless_checkbox.setChecked(True)
        else:
            self.update_versionless_checkbox.setChecked(False)
        self.main_layout.addWidget(self.update_versionless_checkbox, 2, 0, 1, 2)

        self.main_layout.addWidget(self.only_versionless_checkbox, 3, 0, 1, 2)

    def create_edits_widgets(self):

        self.context_edit = QtGui.QLineEdit()
        self.context_edit_label = QtGui.QLabel('Context:')
        self.explicit_file_name_edit = QtGui.QLineEdit()
        self.explicit_file_name_label = QtGui.QLabel('Explicit File Name:')
        self.context_as_file_name_checkbox = QtGui.QCheckBox('Context as File Name')

        self.repo_combo_box = QtGui.QComboBox()
        self.repo_label = QtGui.QLabel('Repository:')

        self.main_layout.addWidget(self.context_edit, 7, 1, 1, 1)
        self.main_layout.addWidget(self.context_edit_label, 7, 0, 1, 1)
        self.main_layout.addWidget(self.explicit_file_name_edit, 8, 1, 1, 1)
        self.main_layout.addWidget(self.explicit_file_name_label, 8, 0, 1, 1)
        self.main_layout.addWidget(self.repo_combo_box, 9, 1, 1, 1)
        self.main_layout.addWidget(self.repo_label, 9, 0, 1, 1)
        self.main_layout.addWidget(self.context_as_file_name_checkbox, 10, 0, 1, 2)

    def create_info_label_widget(self):
        self.info_label_widget = QtGui.QLabel()

        self.info_label_widget.setText(
            'Context: <b>{0}</b>; '
            'Repository: <span style="color:{2};"><b>{1}</b></span>; '.format(
                self.context,
                self.repo['value'][1],
                'rgb({},{},{})'.format(*self.repo['value'][2]),))

        self.main_layout.addWidget(self.info_label_widget, 0, 0, 1, 2)

    def create_label_widget(self):
        self.update_versionless_label = QtGui.QLabel()
        self.main_layout.addWidget(self.update_versionless_label, 1, 0, 1, 2)

    def switch_versionless_label_text(self):
        if self.update_versionless:
            self.update_versionless_label.setText('<p>Versionless files will be <span style="color:#00aa00;"><b>Updated</b></span></p>')
        else:
            self.update_versionless_label.setText('<p>Versionless files will <span style="color:#aa0000;"><b>not be</b></span> Updated</p>')

    def switch_versionless_label(self):

        if self.update_versionless_checkbox.isChecked():
            self.update_versionless = True
            self.collapse_wdg_vls.setVisible(True)
        else:
            self.update_versionless = False
            self.collapse_wdg_vls.setVisible(False)

        self.switch_versionless_label_text()

    def update_virtual_snapshot(self):

        def get_virtual_snapshot_agent():
            info_dict = {
                'status_text': 'Updating Snapshot Info',
                'total_count': 2
            }
            virtual_snapshot_worker.emit_progress(0, info_dict)
            virtual_snapshot = tc.get_virtual_snapshot(
                search_key=self.args_dict['search_key'],
                context=self.args_dict['context'],
                snapshot_type=self.args_dict['snapshot_type'],
                files_dict=self.args_dict['files_dict'],
                is_revision=self.args_dict['is_revision'],
                keep_file_name=self.args_dict['keep_file_name'],
                version=self.args_dict['version'],
                checkin_type=self.args_dict['checkin_type'],
                ignore_keep_file_name=self.args_dict['ignore_keep_file_name'],
                )
            virtual_snapshot_worker.emit_progress(1, info_dict)
            return virtual_snapshot

        virtual_snapshot_worker = gf.get_thread_worker(
            get_virtual_snapshot_agent,
            thread_pool=env_inst.get_thread_pool('commit_queue/server_thread_pool'),
            result_func=self.fill_virtual_snapshot,
            finished_func=self.inplace_chekin,
            progress_func=self.checkin_progress,
            error_func=gf.error_handle
        )
        virtual_snapshot_worker.start()

    def get_virtual_snapshot(self):

        def get_virtual_snapshot_agent():
            info_dict = {
                'status_text': 'Updating Snapshot Info',
                'total_count': 2
            }
            virtual_snapshot_worker.emit_progress(0, info_dict)
            virtual_snapshot = tc.get_virtual_snapshot(
                search_key=self.args_dict['search_key'],
                context=self.args_dict['context'],
                snapshot_type=self.args_dict['snapshot_type'],
                files_dict=self.args_dict['files_dict'],
                is_revision=self.args_dict['is_revision'],
                keep_file_name=self.args_dict['keep_file_name'],
                version=self.args_dict['version'],
                checkin_type=self.args_dict['checkin_type'],
                ignore_keep_file_name=self.args_dict['ignore_keep_file_name'],
                )
            virtual_snapshot_worker.emit_progress(1, info_dict)
            return virtual_snapshot

        virtual_snapshot_worker = gf.get_thread_worker(
            get_virtual_snapshot_agent,
            thread_pool=env_inst.get_thread_pool('commit_queue/server_thread_pool'),
            result_func=self.fill_virtual_snapshot,
            progress_func=self.checkin_progress,
            error_func=gf.error_handle
        )
        virtual_snapshot_worker.start()

    def fill_virtual_snapshot(self, result):
        self.virtual_snapshot = result
        self.fill_versionless_widget(result)
        self.fill_versions_widget(result)
        self.commit_item.set_progress_indicator_off()

    def create_versionless_widget(self):

        self.collapse_wdg_vls = ui_misc_classes.Ui_collapsableWidget(state=True)
        layout_files = QtGui.QVBoxLayout()
        self.collapse_wdg_vls.setLayout(layout_files)
        self.collapse_wdg_vls.setText('Hide Versionless Files')
        self.collapse_wdg_vls.setCollapsedText('Show Versionless Files')

        self.treeWidget_vls = QtGui.QTreeWidget()
        self.treeWidget_vls.setAlternatingRowColors(True)
        self.treeWidget_vls.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.treeWidget_vls.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeWidget_vls.setRootIsDecorated(False)
        self.treeWidget_vls.headerItem().setText(0, "File")
        self.treeWidget_vls.headerItem().setText(1, "Path")
        self.treeWidget_vls.setStyleSheet('QTreeView::item {padding: 2px;}')
        self.treeWidget_vls.setMinimumHeight(150)

        layout_files.addWidget(self.treeWidget_vls)

        self.main_layout.addWidget(self.collapse_wdg_vls, 4, 0, 1, 2)

    def create_versions_widget(self):

        self.collapse_wdg_vers = ui_misc_classes.Ui_collapsableWidget(state=True)
        layout_files = QtGui.QVBoxLayout()
        self.collapse_wdg_vers.setLayout(layout_files)
        self.collapse_wdg_vers.setText('Hide Versions Files')
        self.collapse_wdg_vers.setCollapsedText('Show Versions Files')

        self.treeWidget_vers = QtGui.QTreeWidget()
        self.treeWidget_vers.setAlternatingRowColors(True)
        self.treeWidget_vers.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.treeWidget_vers.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeWidget_vers.setRootIsDecorated(False)
        self.treeWidget_vers.headerItem().setText(0, "File")
        self.treeWidget_vers.headerItem().setText(1, "Path")
        self.treeWidget_vers.setStyleSheet('QTreeView::item {padding: 2px;}')
        self.treeWidget_vers.setMinimumHeight(150)

        layout_files.addWidget(self.treeWidget_vers)

        self.main_layout.addWidget(self.collapse_wdg_vers, 5, 0, 1, 2)

    def fill_versionless_widget(self, paths):
        self.treeWidget_vls.clear()
        for keys, values in paths:
            for i, fl in enumerate(values['versionless']['names']):
                full_path = gf.form_path(self.repo['value'][0] + '/' + values['versionless']['paths'][i])
                item = QtGui.QTreeWidgetItem()
                item.setText(0, ''.join(fl))
                item.setText(1, full_path)
                self.treeWidget_vls.addTopLevelItem(item)
        self.treeWidget_vls.resizeColumnToContents(0)
        self.treeWidget_vls.resizeColumnToContents(1)

    def fill_versions_widget(self, paths):
        self.treeWidget_vers.clear()
        for keys, values in paths:
            for i, fl in enumerate(values['versioned']['names']):
                full_path = gf.form_path(self.repo['value'][0] + '/' + values['versioned']['paths'][i])
                item = QtGui.QTreeWidgetItem()
                item.setText(0, ''.join(fl))
                item.setText(1, full_path)
                self.treeWidget_vers.addTopLevelItem(item)
        self.treeWidget_vers.resizeColumnToContents(0)
        self.treeWidget_vers.resizeColumnToContents(1)

    def create_description_widget(self):

        self.collapse_wdg_descr = ui_misc_classes.Ui_collapsableWidget(state=False)
        layout_files = QtGui.QVBoxLayout()
        self.collapse_wdg_descr.setLayout(layout_files)
        self.collapse_wdg_descr.setText('Hide Description')
        self.collapse_wdg_descr.setCollapsedText('Show Description')

        from lib.ui_classes.ui_checkin_out_classes import Ui_descriptionWidget

        self.description_widget = Ui_descriptionWidget(None, None, parent=self)
        self.description_widget.descriptionTextEdit.setViewportMargins(0, 20, 0, 0)

        self.description_widget.setMinimumHeight(200)
        self.description_widget.setMinimumWidth(400)

        self.description_widget.set_description(self.description)

        layout_files.addWidget(self.description_widget)
        self.main_layout.addWidget(self.collapse_wdg_descr, 6, 0, 1, 2)

        if not self.description:
            self.collapse_wdg_descr.setHidden(True)


class Ui_commitQueueWidget(QtGui.QMainWindow, ui_commit_queue.Ui_commitQueue):
    def __init__(self, project, parent=None):
        super(self.__class__, self).__init__(parent=parent)

        self.project = project
        self.queue_list = []
        self.args_dict_list = []

        self.setupUi(self)

        self.create_ui()

        self.controls_actions()

    def create_ui(self):
        self.setWindowTitle('Commit Queue for Project: {0}'.format(self.project.info.get('title')))
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowStaysOnTopHint)

        server_thread_pool = QtCore.QThreadPool()
        server_thread_pool.setMaxThreadCount(1)
        env_inst.set_thread_pool(server_thread_pool, 'commit_queue/server_thread_pool')

        self.clearQueuePushButton.setIcon(gf.get_icon('trash'))
        self.clearQueuePushButton.setEnabled(False)
        self.commitAllPushButton.setIcon(gf.get_icon('save'))
        self.commitAllPushButton.setEnabled(False)

        self.create_empty_queue_label()

    def controls_actions(self):
        self.filesQueueTreeWidget.itemPressed.connect(self.select_current_commit_widget)
        self.clearQueuePushButton.clicked.connect(self.clear_queue)
        self.closePushButton.clicked.connect(self.close)
        self.commitAllPushButton.clicked.connect(self.commit_queue)

    def create_empty_queue_label(self):
        self.empty_label = QtGui.QLabel()
        self.empty_label.setText('Queue is empty...')
        self.empty_label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.empty_label.setMinimumWidth(450)

        self.commitEditorLayout.addWidget(self.empty_label, 0, 0)

    def select_current_commit_widget(self, tree_item):
        current_item_widget = self.filesQueueTreeWidget.itemWidget(tree_item, 0)
        self.set_current_commit_widget(current_item_widget.get_commit_widget())

    def commit_queue(self):
        self.commitAllPushButton.setEnabled(False)

        next_in_queue = 0
        for commit_item in self.queue_list:
            if commit_item.is_commit_finished():
                next_in_queue += 1

        if next_in_queue < len(self.queue_list):
            commit_item = self.queue_list[next_in_queue]
            commit_widget = commit_item.get_commit_widget()
            commit_widget.commit()

    def clear_queue_after_checkin(self):

        all_committed = False
        for commit_item in self.queue_list:
            all_committed = commit_item.is_commit_finished()

        if all_committed:
            self.clear_queue()
            self.close()

    def clear_queue(self):

        self.filesQueueTreeWidget.clear()
        self.queue_list = []

        self.check_queue()
        self.empty_label.close()
        self.create_empty_queue_label()

    def check_queue(self):

        for i in range(self.commitEditorLayout.count()):
            child = self.commitEditorLayout.takeAt(0)
            if child:
                if child.widget():
                    child.widget().hide()
                    self.commitEditorLayout.removeWidget(child.widget())

        if self.queue_list:
            self.filesCountLabel.setText(str(len(self.queue_list)))
        else:
            self.filesCountLabel.setText('0')

        if self.queue_list and not self.empty_label.isVisible():
            self.empty_label.setVisible(False)
            self.clearQueuePushButton.setEnabled(True)
            self.commitAllPushButton.setEnabled(True)
        else:
            self.empty_label.setVisible(True)
            self.clearQueuePushButton.setEnabled(False)
            self.commitAllPushButton.setEnabled(False)

    def check_for_duplicates(self, args_dict):
        for commit_item in self.queue_list:
            if commit_item.get_args_dict()['file_paths'] == args_dict['file_paths']:
                return True
        return False

    def set_current_commit_widget(self, commit_widget):

        self.check_queue()

        if self.queue_list:
            self.commitEditorLayout.addWidget(commit_widget, 0, 0)
            commit_widget.show()

    def remove_item_from_queue(self, commit_item):
        self.queue_list.remove(commit_item)

    @gf.catch_error
    def add_item_to_queue(self, args_dict):

        if not self.check_for_duplicates(args_dict):
            commit_item = gf.add_commit_item(self.filesQueueTreeWidget, args_dict['item_widget'])
            commit_item.add_args_dict(args_dict)

            self.queue_list.append(commit_item)

            commit_widget = commitWidget(args_dict)

            commit_item.add_commit_widget(commit_widget)
            commit_item.fill_info()

            commit_widget.add_commit_item(commit_item)

            self.set_current_commit_widget(commit_widget)


class saveConfirmWidget(QtGui.QWidget):
    def __init__(self, item_widget, paths, repo, context, update_versionless, description, parent=None):
        super(self.__class__, self).__init__(parent=parent)

        self.item_widget = item_widget
        self.paths = paths
        # print self.paths, 'paths saveConfirmWidget'
        self.repo = repo
        self.context = context
        self.update_versionless = update_versionless
        self.description = description
        self.shown = False

    def create_ui(self):

        self.shown = True
        self.create_main_layout()
        self.create_info_label_widget()
        self.create_label_widget()
        self.create_checkboxes_widget()
        self.create_versionless_widget()
        self.create_versions_widget()

        self.create_description_widget()

        self.switch_versionless_label()

        self.controls_actions()

    def get_data_dict(self):

        data_dict = {
            'description': self.description_widget.get_description('plain'),
            'update_versionless': self.update_versionless_checkbox.isChecked(),
        }

        return data_dict

    def showEvent(self, event):
        if not self.shown:
            self.create_ui()

    def controls_actions(self):
        self.update_versionless_checkbox.stateChanged.connect(self.switch_versionless_label)

    def create_main_layout(self):
        self.main_layout = QtGui.QGridLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def create_checkboxes_widget(self):
        self.update_versionless_checkbox = QtGui.QCheckBox('Update Versionless')
        if self.update_versionless:
            self.update_versionless_checkbox.setChecked(True)
        else:
            self.update_versionless_checkbox.setChecked(False)
        self.main_layout.addWidget(self.update_versionless_checkbox)

    def create_info_label_widget(self):
        self.info_label_widget = QtGui.QLabel()

        self.info_label_widget.setText(
            'Context: <b>{0}</b>; '
            'Repository: <span style="color:{2};"><b>{1}</b></span>; '.format(
                self.context,
                self.repo['value'][1],
                'rgb({},{},{})'.format(*self.repo['value'][2]),))

        self.main_layout.addWidget(self.info_label_widget)

    def create_label_widget(self):
        self.update_versionless_label = QtGui.QLabel()
        self.main_layout.addWidget(self.update_versionless_label)

    def switch_versionless_label_text(self):
        if self.update_versionless:
            self.update_versionless_label.setText('<p>Versionless files will be <span style="color:#00aa00;"><b>Updated</b></span></p>')
        else:
            self.update_versionless_label.setText('<p>Versionless files will <span style="color:#aa0000;"><b>not be</b></span> Updated</p>')

    def switch_versionless_label(self):

        if self.update_versionless_checkbox.isChecked():
            self.update_versionless = True
            self.collapse_wdg_vls.setVisible(True)
        else:
            self.update_versionless = False
            self.collapse_wdg_vls.setVisible(False)

        self.switch_versionless_label_text()

    def create_versionless_widget(self):

        self.collapse_wdg_vls = ui_misc_classes.Ui_collapsableWidget(state=True)
        layout_files = QtGui.QVBoxLayout()
        self.collapse_wdg_vls.setLayout(layout_files)
        self.collapse_wdg_vls.setText('Hide Versionless Files')
        self.collapse_wdg_vls.setCollapsedText('Show Versionless Files')

        # self.files_tree_widget = QtGui.QTreeWidget()
        self.treeWidget_vls = QtGui.QTreeWidget()
        self.treeWidget_vls.setAlternatingRowColors(True)
        self.treeWidget_vls.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.treeWidget_vls.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeWidget_vls.setRootIsDecorated(False)
        self.treeWidget_vls.headerItem().setText(0, "File")
        self.treeWidget_vls.headerItem().setText(1, "Path")
        self.treeWidget_vls.setStyleSheet('QTreeView::item {padding: 2px;}')
        for keys, values in self.paths:
            for i, fl in enumerate(values['versionless']['names']):
                full_path = gf.form_path(self.repo['value'][0] + '/' + values['versionless']['paths'][i])
                item = QtGui.QTreeWidgetItem()
                item.setText(0, ''.join(fl))
                item.setText(1, full_path)
                self.treeWidget_vls.addTopLevelItem(item)
            self.treeWidget_vls.setMinimumWidth(self.treeWidget_vls.columnWidth(0) + self.treeWidget_vls.columnWidth(1) + 150)
        self.treeWidget_vls.setMinimumHeight(250)
        self.treeWidget_vls.resizeColumnToContents(0)
        self.treeWidget_vls.resizeColumnToContents(1)

        layout_files.addWidget(self.treeWidget_vls)

        self.main_layout.addWidget(self.collapse_wdg_vls)

    def create_versions_widget(self):

        self.collapse_wdg_vers = ui_misc_classes.Ui_collapsableWidget(state=True)
        layout_files = QtGui.QVBoxLayout()
        self.collapse_wdg_vers.setLayout(layout_files)
        self.collapse_wdg_vers.setText('Hide Versions Files')
        self.collapse_wdg_vers.setCollapsedText('Show Versions Files')

        # self.files_tree_widget = QtGui.QTreeWidget()
        self.treeWidget_vers = QtGui.QTreeWidget()
        self.treeWidget_vers.setAlternatingRowColors(True)
        self.treeWidget_vers.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.treeWidget_vers.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.treeWidget_vers.setRootIsDecorated(False)
        self.treeWidget_vers.headerItem().setText(0, "File")
        self.treeWidget_vers.headerItem().setText(1, "Path")
        self.treeWidget_vers.setStyleSheet('QTreeView::item {padding: 2px;}')
        for keys, values in self.paths:
            for i, fl in enumerate(values['versioned']['names']):
                full_path = gf.form_path(self.repo['value'][0] + '/' + values['versioned']['paths'][i])
                item = QtGui.QTreeWidgetItem()
                item.setText(0, ''.join(fl))
                item.setText(1, full_path)
                self.treeWidget_vers.addTopLevelItem(item)
            self.treeWidget_vers.setMinimumWidth(self.treeWidget_vers.columnWidth(0) + self.treeWidget_vers.columnWidth(1) + 150)
        self.treeWidget_vers.setMinimumHeight(250)
        self.treeWidget_vers.resizeColumnToContents(0)
        self.treeWidget_vers.resizeColumnToContents(1)

        layout_files.addWidget(self.treeWidget_vers)

        self.main_layout.addWidget(self.collapse_wdg_vers)

    def create_description_widget(self):

        self.collapse_wdg_descr = ui_misc_classes.Ui_collapsableWidget(state=False)
        layout_files = QtGui.QVBoxLayout()
        self.collapse_wdg_descr.setLayout(layout_files)
        self.collapse_wdg_descr.setText('Hide Description')
        self.collapse_wdg_descr.setCollapsedText('Show Description')

        from lib.ui_classes.ui_checkin_out_classes import Ui_descriptionWidget

        self.description_widget = Ui_descriptionWidget(None, None, parent=self)
        self.description_widget.descriptionTextEdit.setViewportMargins(0, 20, 0, 0)

        self.description_widget.setMinimumHeight(200)
        self.description_widget.setMinimumWidth(400)

        self.description_widget.set_description(self.description)

        layout_files.addWidget(self.description_widget)
        self.main_layout.addWidget(self.collapse_wdg_descr)

        if not self.description:
            self.collapse_wdg_descr.setHidden(True)
