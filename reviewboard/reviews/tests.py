from __future__ import print_function, unicode_literals

from django.utils import six
from kgb import SpyAgency
from reviewboard.reviews.markdown_utils import (markdown_escape,
                                                markdown_unescape)
from reviewboard.reviews.models import (Comment,
                                        DefaultReviewer,
                                        Group,
                                        ReviewRequest,
                                        ReviewRequestDraft,
                                        Review,
                                        Screenshot)
from reviewboard.scmtools.core import Commit
from reviewboard.testing import TestCase
    fixtures = ['test_users']
        user1 = User.objects.get(username='doc')
        user2 = User.objects.get(username='grumpy')

        self.create_review_request(summary='Test 1',
                                   publish=True,
                                   submitter=user1)
        self.create_review_request(summary='Test 2',
                                   submitter=user2)
        self.create_review_request(summary='Test 3',
                                   status='S',
                                   public=True,
                                   submitter=user1)
        self.create_review_request(summary='Test 4',
                                   status='S',
                                   public=True,
                                   submitter=user2)
        self.create_review_request(summary='Test 5',
                                   status='D',
                                   public=True,
                                   submitter=user1)
        self.create_review_request(summary='Test 6',
                                   status='D',
                                   submitter=user2)

            ReviewRequest.objects.public(user=user1),
            [
                'Test 1',
            ])
            ReviewRequest.objects.public(status=None),
            [
                'Test 5',
                'Test 4',
                'Test 3',
                'Test 1',
            ])
            ReviewRequest.objects.public(user=user2, status=None),
            [
                'Test 6',
                'Test 5',
                'Test 4',
                'Test 3',
                'Test 2',
                'Test 1'
            ])
        review_request =self.create_review_request(repository=repository,
                                                   publish=True)
        user1 = User.objects.get(username='doc')

        group1 = self.create_review_group(name='privgroup')
        group1.users.add(user1)

        review_request = self.create_review_request(summary='Test 1',
                                                    public=True,
                                                    submitter=user1)
        review_request.target_groups.add(group1)

        review_request = self.create_review_request(summary='Test 2',
                                                    public=False,
                                                    submitter=user1)
        review_request.target_groups.add(group1)

        review_request = self.create_review_request(summary='Test 3',
                                                    public=True,
                                                    status='S',
                                                    submitter=user1)
        review_request.target_groups.add(group1)

            [
                'Test 1',
            ])
            [
                'Test 3',
                'Test 1',
            ])
        user1 = User.objects.get(username='doc')
        user2 = User.objects.get(username='grumpy')

        group1 = self.create_review_group(name='group1')
        group1.users.add(user1)

        group2 = self.create_review_group(name='group2')
        group2.users.add(user2)

        review_request = self.create_review_request(summary='Test 1',
                                                    public=True,
                                                    submitter=user1)
        review_request.target_groups.add(group1)

        review_request = self.create_review_request(summary='Test 2',
                                                    submitter=user2,
                                                    public=True,
                                                    status='S')
        review_request.target_groups.add(group1)

        review_request = self.create_review_request(summary='Test 3',
                                                    public=True,
                                                    submitter=user2)
        review_request.target_groups.add(group1)
        review_request.target_groups.add(group2)

            [
                'Test 3',
                'Test 1',
            ])
            ReviewRequest.objects.to_user_groups(
                "doc", status=None, local_site=None),
            [
                'Test 3',
                'Test 2',
                'Test 1',
            ])
            ReviewRequest.objects.to_user_groups(
                "grumpy", user=user2, local_site=None),
            [
                'Test 3',
            ])
        user1 = User.objects.get(username='doc')
        user2 = User.objects.get(username='grumpy')

        group1 = self.create_review_group(name='group1')
        group1.users.add(user1)

        group2 = self.create_review_group(name='group2')
        group2.users.add(user2)

        review_request = self.create_review_request(summary='Test 1',
                                                    public=True,
                                                    submitter=user1)
        review_request.target_groups.add(group1)
        review_request.target_people.add(user2)

        review_request = self.create_review_request(summary='Test 2',
                                                    submitter=user2,
                                                    status='S')
        review_request.target_groups.add(group1)
        review_request.target_people.add(user2)
        review_request.target_people.add(user1)

        review_request = self.create_review_request(summary='Test 3',
                                                    public=True,
                                                    submitter=user2)
        review_request.target_groups.add(group1)
        review_request.target_groups.add(group2)
        review_request.target_people.add(user1)

        review_request = self.create_review_request(summary='Test 4',
                                                    public=True,
                                                    status='S',
                                                    submitter=user2)
        review_request.target_people.add(user1)

            [
                'Test 3',
            ])
            [
                'Test 4',
                'Test 3',
            ])
            ReviewRequest.objects.to_user_directly(
                "doc", user2, status=None, local_site=None),
            [
                'Test 4',
                'Test 3',
                'Test 2',
            ])
        user1 = User.objects.get(username='doc')

        self.create_review_request(summary='Test 1',
                                   public=True,
                                   submitter=user1)

        self.create_review_request(summary='Test 2',
                                   public=False,
                                   submitter=user1)

        self.create_review_request(summary='Test 3',
                                   public=True,
                                   status='S',
                                   submitter=user1)

            ReviewRequest.objects.from_user("doc", local_site=None),
            [
                'Test 1',
            ])
            ReviewRequest.objects.from_user("doc", status=None,
                                            local_site=None),
            [
                'Test 3',
                'Test 1',
            ])
            ReviewRequest.objects.from_user(
                "doc", user=user1, status=None, local_site=None),
            [
                'Test 3',
                'Test 2',
                'Test 1',
            ])
        user1 = User.objects.get(username='doc')
        user2 = User.objects.get(username='grumpy')

        group1 = self.create_review_group(name='group1')
        group1.users.add(user1)

        group2 = self.create_review_group(name='group2')
        group2.users.add(user2)

        review_request = self.create_review_request(summary='Test 1',
                                                    publish=True,
                                                    submitter=user1)
        review_request.target_groups.add(group1)

        review_request = self.create_review_request(summary='Test 2',
                                                    submitter=user2,
                                                    status='S')
        review_request.target_groups.add(group1)
        review_request.target_people.add(user2)
        review_request.target_people.add(user1)

        review_request = self.create_review_request(summary='Test 3',
                                                    publish=True,
                                                    submitter=user2)
        review_request.target_groups.add(group1)
        review_request.target_groups.add(group2)
        review_request.target_people.add(user1)

        review_request = self.create_review_request(summary='Test 4',
                                                    publish=True,
                                                    status='S',
                                                    submitter=user2)
        review_request.target_groups.add(group1)
        review_request.target_groups.add(group2)
        review_request.target_people.add(user1)
            ReviewRequest.objects.to_user("doc", local_site=None),
            [
                'Test 3',
                'Test 1',
            ])
        self.assertValidSummaries(
            ReviewRequest.objects.to_user("doc", status=None, local_site=None),
            [
                'Test 4',
                'Test 3',
                'Test 1',
            ])
            ReviewRequest.objects.to_user(
                "doc", user=user2, status=None, local_site=None),
            [
                'Test 4',
                'Test 3',
                'Test 2',
                'Test 1',
            ])
            self.assertTrue(summary in summaries,
                            'summary "%s" not found in summary list'
                            % summary)
            self.assertTrue(summary in r_summaries,
                            'summary "%s" not found in review request list'
                            % summary)
    fixtures = ['test_users', 'test_scmtools', 'test_site']
        super(ViewTests, self).setUp()

        review_request = self.create_review_request(publish=True)
        username = 'admin'
        summary = 'This is a test summary'
        description = 'This is my description'
        testing_done = 'Some testing'
        review_request = self.create_review_request(
            publish=True,
            submitter=username,
            summary=summary,
            description=description,
            testing_done=testing_done)
        response = self.client.get('/r/%s/' % review_request.pk)
        self.assertEqual(response.status_code, 200)
        request = self.getContextVar(response, 'review_request')
        self.assertEqual(request.submitter.username, username)
        self.assertEqual(request.summary, summary)
        self.assertEqual(request.description, description)
        self.assertEqual(request.testing_done, testing_done)
        self.assertEqual(request.pk, review_request.pk)
        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
        diffset = self.create_diffset(review_request)
        filediff = self.create_filediff(diffset)
        main_review = self.create_review(review_request, user=user1)
        main_comment = self.create_diff_comment(main_review, filediff,
                                                text=comment_text_1)
        reply1 = self.create_reply(
            main_review,
            user=user1,
            timestamp=(main_review.timestamp + timedelta(days=1)))
        self.create_diff_comment(reply1, filediff, text=comment_text_2,
                                 reply_to=main_comment)
        reply2 = self.create_reply(
            main_review,
            user=user2,
            timestamp=(main_review.timestamp + timedelta(days=2)))
        self.create_diff_comment(reply2, filediff, text=comment_text_3,
                                 reply_to=main_comment)

        self.create_review_request(publish=True)

        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
        diffset = self.create_diffset(review_request, revision=1)
        self.create_filediff(
            diffset,
            source_file='/diffutils.py',
            dest_file='/diffutils.py',
            source_revision='6bba278',
            dest_detail='465d217',
            diff=(
                b'diff --git a/diffutils.py b/diffutils.py\n'
                b'index 6bba278..465d217 100644\n'
                b'--- a/diffutils.py\n'
                b'+++ b/diffutils.py\n'
                b'@@ -1,3 +1,4 @@\n'
                b'+# diffutils.py\n'
                b' import fnmatch\n'
                b' import os\n'
                b' import re\n'
            ))
        self.create_filediff(
            diffset,
            source_file='/readme',
            dest_file='/readme',
            source_revision='d6613f5',
            dest_detail='5b50866',
            diff=(
                b'diff --git a/readme b/readme\n'
                b'index d6613f5..5b50866 100644\n'
                b'--- a/readme\n'
                b'+++ b/readme\n'
                b'@@ -1 +1,3 @@\n'
                b' Hello there\n'
                b'+\n'
                b'+Oh hi!\n'
            ))
        self.create_filediff(
            diffset,
            source_file='/newfile',
            dest_file='/newfile',
            source_revision='PRE-CREATION',
            dest_detail='',
            diff=(
                b'diff --git a/new_file b/new_file\n'
                b'new file mode 100644\n'
                b'index 0000000..ac30bd3\n'
                b'--- /dev/null\n'
                b'+++ b/new_file\n'
                b'@@ -0,0 +1 @@\n'
                b'+This is a new file!\n'
            ))

        diffset = self.create_diffset(review_request, revision=2)
        self.create_filediff(
            diffset,
            source_file='/diffutils.py',
            dest_file='/diffutils.py',
            source_revision='6bba278',
            dest_detail='465d217',
            diff=(
                b'diff --git a/diffutils.py b/diffutils.py\n'
                b'index 6bba278..465d217 100644\n'
                b'--- a/diffutils.py\n'
                b'+++ b/diffutils.py\n'
                b'@@ -1,3 +1,4 @@\n'
                b'+# diffutils.py\n'
                b' import fnmatch\n'
                b' import os\n'
                b' import re\n'
            ))
        self.create_filediff(
            diffset,
            source_file='/readme',
            dest_file='/readme',
            source_revision='d6613f5',
            dest_detail='5b50867',
            diff=(
                b'diff --git a/readme b/readme\n'
                b'index d6613f5..5b50867 100644\n'
                b'--- a/readme\n'
                b'+++ b/readme\n'
                b'@@ -1 +1,3 @@\n'
                b' Hello there\n'
                b'+----------\n'
                b'+Oh hi!\n'
            ))
        self.create_filediff(
            diffset,
            source_file='/newfile',
            dest_file='/newfile',
            source_revision='PRE-CREATION',
            dest_detail='',
            diff=(
                b'diff --git a/new_file b/new_file\n'
                b'new file mode 100644\n'
                b'index 0000000..ac30bd4\n'
                b'--- /dev/null\n'
                b'+++ b/new_file\n'
                b'@@ -0,0 +1 @@\n'
                b'+This is a diffent version of this new file!\n'
            ))

        response = self.client.get('/r/1/diff/1-2/')
            print("Error: %s" % self.getContextVar(response, 'error'))
            print(self.getContextVar(response, 'trace'))
        self.assertEqual(
            self.getContextVar(response, 'diff_context')['num_diffs'],
            2)
        self.assertTrue(files)
        self.assertEqual(files[0]['depot_filename'], '/newfile')
        self.assertTrue('interfilediff' in files[0])
        self.assertEqual(files[1]['depot_filename'], '/readme')
        self.assertTrue('interfilediff' in files[1])
        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
        diffset = self.create_diffset(review_request, revision=1)
        self.create_filediff(
            diffset,
            source_file='/diffutils.py',
            dest_file='/diffutils.py',
            source_revision='6bba278',
            dest_detail='465d217',
            diff=(
                b'diff --git a/diffutils.py b/diffutils.py\n'
                b'index 6bba278..465d217 100644\n'
                b'--- a/diffutils.py\n'
                b'+++ b/diffutils.py\n'
                b'@@ -1,3 +1,4 @@\n'
                b'+# diffutils.py\n'
                b' import fnmatch\n'
                b' import os\n'
                b' import re\n'
            ))

        diffset = self.create_diffset(review_request, revision=2)
        self.create_filediff(
            diffset,
            source_file='/diffutils.py',
            dest_file='/diffutils.py',
            source_revision='6bba278',
            dest_detail='465d217',
            diff=(
                b'diff --git a/diffutils.py b/diffutils.py\n'
                b'index 6bba278..465d217 100644\n'
                b'--- a/diffutils.py\n'
                b'+++ b/diffutils.py\n'
                b'@@ -1,3 +1,4 @@\n'
                b'+# diffutils.py\n'
                b' import fnmatch\n'
                b' import os\n'
                b' import re\n'
            ))
        self.create_filediff(
            diffset,
            source_file='/newfile',
            dest_file='/newfile',
            source_revision='PRE-CREATION',
            dest_detail='',
            diff=(
                b'diff --git a/new_file b/new_file\n'
                b'new file mode 100644\n'
                b'index 0000000..ac30bd4\n'
                b'--- /dev/null\n'
                b'+++ b/new_file\n'
                b'@@ -0,0 +1 @@\n'
                b'+This is a diffent version of this new file!\n'
            ))

        response = self.client.get('/r/1/diff/1-2/')
            print("Error: %s" % self.getContextVar(response, 'error'))
            print(self.getContextVar(response, 'trace'))
        self.assertEqual(
            self.getContextVar(response, 'diff_context')['num_diffs'],
            2)
        self.assertTrue(files)
        self.assertEqual(files[0]['depot_filename'], '/newfile')
        self.assertTrue('interfilediff' in files[0])
        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
        diffset = self.create_diffset(review_request)
        filediff = self.create_filediff(diffset)
        review = self.create_review(review_request, user=user)
        comment = self.create_diff_comment(review, filediff,
                                           issue_opened=True)
    fixtures = ['test_users', 'test_scmtools']
        self.assertTrue("summary" in fields)
        self.assertTrue("description" in fields)
        self.assertTrue("testing_done" in fields)
        self.assertTrue("branch" in fields)
        self.assertTrue("bugs_closed" in fields)
        review_request = self.create_review_request(publish=True)
        return ReviewRequestDraft.create(review_request)
    def test_long_bug_numbers(self):
    def test_no_summary(self):
        lower(review_request)

    @add_fixtures(['test_users'])
    def test_commit_id(self):
        """Testing commit_id migration"""
        review_request = self.create_review_request()
        review_request.changenum = '123'

        self.assertEqual(review_request.commit_id, None)
        self.assertEqual(review_request.commit,
                         six.text_type(review_request.changenum))
        self.assertNotEqual(review_request.commit_id, None)


class PostCommitTests(SpyAgency, TestCase):
    fixtures = ['test_users', 'test_scmtools']

    def setUp(self):
        super(PostCommitTests, self).setUp()

        self.user = User.objects.create(username='testuser', password='')
        self.profile, is_new = Profile.objects.get_or_create(user=self.user)
        self.profile.save()

        self.testdata_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'scmtools', 'testdata')

        self.repository = self.create_repository(tool_name='Test')

    def test_update_from_committed_change(self):
        """Testing post-commit update"""
        commit_id = '4'

        def get_change(repository, commit_to_get):
            self.assertEqual(commit_id, commit_to_get)

            commit = Commit()
            commit.message = \
                'This is my commit message\n\nWith a summary line too.'
            diff_filename = os.path.join(self.testdata_dir, 'git_readme.diff')
            with open(diff_filename, 'r') as f:
                commit.diff = f.read()

            return commit

        def get_file_exists(repository, path, revision, base_commit_id=None,
                            request=None):
            return (path, revision) in [('/readme', 'd6613f5')]

        self.spy_on(self.repository.get_change, call_fake=get_change)
        self.spy_on(self.repository.get_file_exists, call_fake=get_file_exists)

        review_request = ReviewRequest.objects.create(self.user,
                                                      self.repository)
        review_request.update_from_commit_id(commit_id)

        self.assertEqual(review_request.summary, 'This is my commit message')
        self.assertEqual(review_request.description,
                         'With a summary line too.')

        self.assertEqual(review_request.diffset_history.diffsets.count(), 1)

        diffset = review_request.diffset_history.diffsets.get()
        self.assertEqual(diffset.files.count(), 1)

        fileDiff = diffset.files.get()
        self.assertEqual(fileDiff.source_file, '/readme')
        self.assertEqual(fileDiff.source_revision, 'd6613f5')

    def test_update_from_committed_change_with_markdown_escaping(self):
        """Testing post-commit update with markdown escaping"""
        def get_change(repository, commit_to_get):
            commit = Commit()
            commit.message = '* No escaping\n\n* but this needs escaping'
            diff_filename = os.path.join(self.testdata_dir, 'git_readme.diff')
            with open(diff_filename, 'r') as f:
                commit.diff = f.read()

            return commit

        def get_file_exists(repository, path, revision, base_commit_id=None,
                            request=None):
            return (path, revision) in [('/readme', 'd6613f5')]

        self.spy_on(self.repository.get_change, call_fake=get_change)
        self.spy_on(self.repository.get_file_exists, call_fake=get_file_exists)

        review_request = ReviewRequest.objects.create(self.user,
                                                      self.repository)
        review_request.rich_text = True
        review_request.update_from_commit_id('4')

        self.assertEqual(review_request.summary, '* No escaping')
        self.assertEqual(review_request.description,
                         '\\* but this needs escaping')

    def test_update_from_committed_change_without_repository_support(self):
        """Testing post-commit update failure conditions"""
        self.spy_on(self.repository.__class__.supports_post_commit.fget,
                    call_fake=lambda self: False)
        review_request = ReviewRequest.objects.create(self.user,
                                                      self.repository)

        self.assertRaises(NotImplementedError,
                          lambda: review_request.update_from_commit_id('4'))
    fixtures = ['test_users', 'test_scmtools']
        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
        diffset = self.create_diffset(review_request)
        filediff = self.create_filediff(diffset)
        master_review = self.create_review(review_request, user=user,
                                           body_top=body_top,
                                           body_bottom='')
        self.create_diff_comment(master_review, filediff, text=comment_text_1,
                                 first_line=1, num_lines=1)
        review = self.create_review(review_request, user=user,
                                    body_top='', body_bottom='')
        self.create_diff_comment(review, filediff, text=comment_text_2,
                                 first_line=1, num_lines=1)
        review = self.create_review(review_request, user=user,
                                    body_top='',
                                    body_bottom=body_bottom)
        self.create_diff_comment(review, filediff, text=comment_text_3,
                                 first_line=1, num_lines=1)
        self.assertTrue(review)
        self.assertEqual(len(default_reviewers), 2)
        self.assertTrue(default_reviewer1 in default_reviewers)
        self.assertTrue(default_reviewer2 in default_reviewers)
        self.assertEqual(len(default_reviewers), 1)
        self.assertTrue(default_reviewer2 in default_reviewers)
        default_reviewers = DefaultReviewer.objects.for_repository(
            None, test_site)
        self.assertEqual(len(default_reviewers), 1)
        self.assertTrue(default_reviewer1 in default_reviewers)
        self.assertEqual(len(default_reviewers), 1)
        self.assertTrue(default_reviewer2 in default_reviewers)
            "{% ifneatnumber " + six.text_type(rid) + " %}"
class ReviewRequestCounterTests(TestCase):
        super(ReviewRequestCounterTests, self).setUp()

class IssueCounterTests(TestCase):
    fixtures = ['test_users']

    def setUp(self):
        super(IssueCounterTests, self).setUp()

        self.review_request = self.create_review_request(publish=True)
        self.assertEqual(self.review_request.issue_open_count, 0)
        self.assertEqual(self.review_request.issue_resolved_count, 0)
        self.assertEqual(self.review_request.issue_dropped_count, 0)

        self._reset_counts()

    @add_fixtures(['test_scmtools'])
    def test_init_with_diff_comments(self):
        """Testing ReviewRequest issue counter initialization
        from diff comments
        """
        self.review_request.repository = self.create_repository()

        diffset = self.create_diffset(self.review_request)
        filediff = self.create_filediff(diffset)

        self._test_issue_counts(
            lambda review, issue_opened: self.create_diff_comment(
                review, filediff, issue_opened=issue_opened))

    def test_init_with_file_attachment_comments(self):
        """Testing ReviewRequest issue counter initialization
        from file attachment comments
        """
        file_attachment = self.create_file_attachment(self.review_request)

        self._test_issue_counts(
            lambda review, issue_opened: self.create_file_attachment_comment(
                review, file_attachment, issue_opened=issue_opened))

    def test_init_with_screenshot_comments(self):
        """Testing ReviewRequest issue counter initialization
        from screenshot comments
        """
        screenshot = self.create_screenshot(self.review_request)

        self._test_issue_counts(
            lambda review, issue_opened: self.create_screenshot_comment(
                review, screenshot, issue_opened=issue_opened))

    @add_fixtures(['test_scmtools'])
    def test_init_with_mix(self):
        """Testing ReviewRequest issue counter initialization
        from multiple types of comments at once
        """
        # The initial implementation for issue status counting broke when
        # there were multiple types of comments on a review (such as diff
        # comments and file attachment comments). There would be an
        # artificially large number of issues reported.
        #
        # That's been fixed, and this test is ensuring that it doesn't
        # regress.
        self.review_request.repository = self.create_repository()
        diffset = self.create_diffset(self.review_request)
        filediff = self.create_filediff(diffset)
        file_attachment = self.create_file_attachment(self.review_request)
        screenshot = self.create_screenshot(self.review_request)

        review = self.create_review(self.review_request)

        # One open file attachment comment
        self.create_file_attachment_comment(review, file_attachment,
                                            issue_opened=True)

        # Two diff comments
        self.create_diff_comment(review, filediff, issue_opened=True)
        self.create_diff_comment(review, filediff, issue_opened=True)

        # Four screenshot comments
        self.create_screenshot_comment(review, screenshot, issue_opened=True)
        self.create_screenshot_comment(review, screenshot, issue_opened=True)
        self.create_screenshot_comment(review, screenshot, issue_opened=True)
        self.create_screenshot_comment(review, screenshot, issue_opened=True)

        # The issue counts should be end up being 0, since they'll initialize
        # during load.
        self._reload_object(clear_counters=True)
        self.assertEqual(self.review_request.issue_open_count, 0)
        self.assertEqual(self.review_request.issue_resolved_count, 0)
        self.assertEqual(self.review_request.issue_dropped_count, 0)

        # Now publish. We should have 7 open issues, by way of incrementing
        # during publish.
        review.publish()

        self._reload_object()
        self.assertEqual(self.review_request.issue_open_count, 7)
        self.assertEqual(self.review_request.issue_dropped_count, 0)
        self.assertEqual(self.review_request.issue_resolved_count, 0)

        # Make sure we get the same number back when initializing counters.
        self._reload_object(clear_counters=True)
        self.assertEqual(self.review_request.issue_open_count, 7)
        self.assertEqual(self.review_request.issue_dropped_count, 0)
        self.assertEqual(self.review_request.issue_resolved_count, 0)

    def test_init_with_replies(self):
        """Testing ReviewRequest issue counter initialization and replies."""
        file_attachment = self.create_file_attachment(self.review_request)

        review = self.create_review(self.review_request)
        comment = self.create_file_attachment_comment(review, file_attachment,
                                                      issue_opened=True)
        review.publish()

        reply = self.create_reply(review)
        self.create_file_attachment_comment(reply, file_attachment,
                                            reply_to=comment,
                                            issue_opened=True)
        reply.publish()

        self._reload_object(clear_counters=True)
        self.assertEqual(self.review_request.issue_open_count, 1)
        self.assertEqual(self.review_request.issue_resolved_count, 0)
        self.assertEqual(self.review_request.issue_dropped_count, 0)

    def test_save_reply_comment(self):
        """Testing ReviewRequest issue counter and saving reply comments."""
        file_attachment = self.create_file_attachment(self.review_request)

        review = self.create_review(self.review_request)
        comment = self.create_file_attachment_comment(review, file_attachment,
                                                      issue_opened=True)
        review.publish()

        self._reload_object(clear_counters=True)
        self.assertEqual(self.review_request.issue_open_count, 1)
        self.assertEqual(self.review_request.issue_resolved_count, 0)
        self.assertEqual(self.review_request.issue_dropped_count, 0)

        reply = self.create_reply(review)
        reply_comment = self.create_file_attachment_comment(
            reply, file_attachment,
            reply_to=comment,
            issue_opened=True)
        reply.publish()

        self._reload_object()
        self.assertEqual(self.review_request.issue_open_count, 1)
        self.assertEqual(self.review_request.issue_resolved_count, 0)
        self.assertEqual(self.review_request.issue_dropped_count, 0)

        reply_comment.save()
        self._reload_object()
        self.assertEqual(self.review_request.issue_open_count, 1)
        self.assertEqual(self.review_request.issue_resolved_count, 0)
        self.assertEqual(self.review_request.issue_dropped_count, 0)

    def _test_issue_counts(self, create_comment_func):
        review = self.create_review(self.review_request)

        # One comment without an issue opened.
        create_comment_func(review, issue_opened=False)

        # Three comments with an issue opened.
        for i in range(3):
            create_comment_func(review, issue_opened=True)

        # Two comments that will have their issues dropped.
        dropped_comments = [
            create_comment_func(review, issue_opened=True)
            for i in range(2)
        ]

        # One comment that will have its issue resolved.
        resolved_comments = [
            create_comment_func(review, issue_opened=True)
        ]

        # The issue counts should be end up being 0, since they'll initialize
        # during load.
        self._reload_object(clear_counters=True)
        self.assertEqual(self.review_request.issue_open_count, 0)
        self.assertEqual(self.review_request.issue_resolved_count, 0)
        self.assertEqual(self.review_request.issue_dropped_count, 0)

        # Now publish. We should have 6 open issues, by way of incrementing
        # during publish.
        review.publish()

        self._reload_object()
        self.assertEqual(self.review_request.issue_open_count, 6)
        self.assertEqual(self.review_request.issue_dropped_count, 0)
        self.assertEqual(self.review_request.issue_resolved_count, 0)

        # Make sure we get the same number back when initializing counters.
        self._reload_object(clear_counters=True)
        self.assertEqual(self.review_request.issue_open_count, 6)
        self.assertEqual(self.review_request.issue_dropped_count, 0)
        self.assertEqual(self.review_request.issue_resolved_count, 0)

        # Set the issue statuses.
        for comment in dropped_comments:
            comment.issue_status = Comment.DROPPED
            comment.save()

        for comment in resolved_comments:
            comment.issue_status = Comment.RESOLVED
            comment.save()

        self._reload_object()
        self.assertEqual(self.review_request.issue_open_count, 3)
        self.assertEqual(self.review_request.issue_dropped_count, 2)
        self.assertEqual(self.review_request.issue_resolved_count, 1)

        # Make sure we get the same number back when initializing counters.
        self._reload_object(clear_counters=True)
        self.assertEqual(self.review_request.issue_open_count, 3)
        self.assertEqual(self.review_request.issue_dropped_count, 2)
        self.assertEqual(self.review_request.issue_resolved_count, 1)

    def _reload_object(self, clear_counters=False):
        if clear_counters:
            # 3 queries: One for the review request fetch, one for
            # the issue status load, and one for updating the issue counts.
            expected_query_count = 3
            self._reset_counts()
        else:
            # One query for the review request fetch.
            expected_query_count = 1

        with self.assertNumQueries(expected_query_count):
            self.review_request = \
                ReviewRequest.objects.get(pk=self.review_request.pk)

    def _reset_counts(self):
        self.review_request.issue_open_count = None
        self.review_request.issue_resolved_count = None
        self.review_request.issue_dropped_count = None
        self.review_request.save()


    fixtures = ['test_users']
        super(PolicyTests, self).setUp()

        review_request = self.create_review_request(publish=True,
                                                    submitter=self.user)
    @add_fixtures(['test_scmtools'])
    @add_fixtures(['test_scmtools'])
    @add_fixtures(['test_scmtools'])
    @add_fixtures(['test_scmtools'])
        review_request = self.create_review_request(publish=True)
        review_request = self.create_review_request(publish=True)
        review_request = self.create_review_request(publish=True)
    @add_fixtures(['test_scmtools'])
        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
    @add_fixtures(['test_scmtools'])
        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
    @add_fixtures(['test_scmtools'])
        review_request = self.create_review_request(create_repository=True,
                                                    publish=True)
        user.first_name = 'Test\u21b9'
        user.last_name = 'User\u2729'


class MarkdownUtilsTests(TestCase):
    UNESCAPED_TEXT = r'\`*_{}[]()>#+-.!'
    ESCAPED_TEXT = r'\\\`\*\_\{\}\[\]\(\)\>#+-.\!'

    def test_markdown_escape(self):
        """Testing markdown_escape"""
        self.assertEqual(markdown_escape(self.UNESCAPED_TEXT),
                         self.ESCAPED_TEXT)

    def test_markdown_escape_periods(self):
        """Testing markdown_escape with '.' placement"""
        self.assertEqual(
            markdown_escape('Line. 1.\n'
                            '1. Line. 2.\n'
                            '1.2. Line. 3.\n'
                            '  1. Line. 4.'),
            ('Line. 1.\n'
             '1\\. Line. 2.\n'
             '1\\.2\\. Line. 3.\n'
             '  1\\. Line. 4.'))

    def test_markdown_escape_atx_headers(self):
        """Testing markdown_escape with '#' placement"""
        self.assertEqual(
            markdown_escape('### Header\n'
                            '  ## Header ##\n'
                            'Not # a header'),
            ('\\#\\#\\# Header\n'
             '  \\#\\# Header ##\n'
             'Not # a header'))

    def test_markdown_escape_hyphens(self):
        """Testing markdown_escape with '-' placement"""
        self.assertEqual(
            markdown_escape('Header\n'
                            '------\n'
                            '\n'
                            '- List item\n'
                            '  - List item\n'
                            'Just hyp-henated'),
            ('Header\n'
             '\\-\\-\\-\\-\\-\\-\n'
             '\n'
             '\\- List item\n'
             '  \\- List item\n'
             'Just hyp-henated'))

    def test_markdown_escape_plusses(self):
        """Testing markdown_escape with '+' placement"""
        self.assertEqual(
            markdown_escape('+ List item\n'
                            'a + b'),
            ('\\+ List item\n'
             'a + b'))

    def test_markdown_escape_underscores(self):
        """Testing markdown_escape with '_' placement"""
        self.assertEqual(markdown_escape('_foo_'), r'\_foo\_')
        self.assertEqual(markdown_escape('__foo__'), r'\_\_foo\_\_')
        self.assertEqual(markdown_escape(' _foo_ '), r' \_foo\_ ')
        self.assertEqual(markdown_escape('f_o_o'), r'f_o_o')
        self.assertEqual(markdown_escape('f_o_o_'), r'f_o_o\_')
        self.assertEqual(markdown_escape('foo_ _bar'), r'foo\_ \_bar')
        self.assertEqual(markdown_escape('foo__bar'), r'foo__bar')
        self.assertEqual(markdown_escape('foo\n_bar'), 'foo\n\\_bar')
        self.assertEqual(markdown_escape('(_foo_)'), r'(\_foo\_)')

    def test_markdown_escape_asterisks(self):
        """Testing markdown_escape with '*' placement"""
        self.assertEqual(markdown_escape('*foo*'), r'\*foo\*')
        self.assertEqual(markdown_escape('**foo**'), r'\*\*foo\*\*')
        self.assertEqual(markdown_escape(' *foo* '), r' \*foo\* ')
        self.assertEqual(markdown_escape('f*o*o'), r'f*o*o')
        self.assertEqual(markdown_escape('f*o*o*'), r'f*o*o\*')
        self.assertEqual(markdown_escape('foo* *bar'), r'foo\* \*bar')
        self.assertEqual(markdown_escape('foo**bar'), r'foo**bar')
        self.assertEqual(markdown_escape('foo\n*bar'), 'foo\n\\*bar')

    def test_markdown_escape_parens(self):
        """Testing markdown_escape with '(' and ')' placement"""
        self.assertEqual(markdown_escape('[name](link)'), r'\[name\]\(link\)')
        self.assertEqual(markdown_escape('(link)'), r'(link)')
        self.assertEqual(markdown_escape('](link)'), r'\](link)')
        self.assertEqual(markdown_escape('[foo] ](link)'),
                         r'\[foo\] \](link)')

    def test_markdown_unescape(self):
        """Testing markdown_unescape"""
        self.assertEqual(markdown_unescape(self.ESCAPED_TEXT),
                         self.UNESCAPED_TEXT)