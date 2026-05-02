# API Reliability Monitor — SLA Report

> Last updated: **2026-05-02 11:57 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.3%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 56.06% | 4583.8 | 10206.7 | 1000ms | 261/594 |
| ❌ | `public_apis_list` | 0.0% | 99.66% | 123.4 | 4088.9 | 1500ms | 2/594 |
| ❌ | `nasa_apod` | 69.02% | 46.63% | 3717.8 | 10549.1 | 2000ms | 317/594 |
| ❌ | `ipapi_check` | 87.71% | 100.0% | 156.0 | 353.0 | 2500ms | 0/594 |
| ⚠️ | `rest_countries` | 98.48% | 98.32% | 344.1 | 10221.5 | 2500ms | 10/594 |
| ⚠️ | `open_meteo_weather` | 98.65% | 97.31% | 714.4 | 14877.1 | 2000ms | 16/594 |
| ⚠️ | `dog_ceo_random` | 99.49% | 92.93% | 729.6 | 10244.1 | 2500ms | 42/594 |
| ✅ | `catfact_random` | 99.49% | 99.49% | 248.9 | 10080.2 | 3000ms | 3/594 |
| ✅ | `coingecko_bitcoin` | 99.49% | 100.0% | 98.7 | 252.0 | 1500ms | 0/594 |
| ✅ | `useless_fact` | 99.66% | 99.33% | 585.4 | 10229.6 | 2500ms | 4/594 |
| ✅ | `agify_name` | 100.0% | 99.83% | 369.1 | 3237.1 | 2000ms | 1/594 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.66% | 237.7 | 3882.8 | 2000ms | 2/594 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6148.6 | 60.0% |
| `numbers_trivia` | 12:00 | 5382.0 | 52.0% |
| `nasa_apod` | 17:00 | 5222.7 | 64.71% |
| `numbers_trivia` | 03:00 | 5199.6 | 50.0% |
| `numbers_trivia` | 18:00 | 5196.2 | 50.0% |
| `numbers_trivia` | 01:00 | 5126.1 | 50.0% |
| `nasa_apod` | 03:00 | 5080.8 | 81.25% |
| `numbers_trivia` | 10:00 | 4972.0 | 48.0% |
| `numbers_trivia` | 07:00 | 4955.2 | 47.62% |
| `numbers_trivia` | 14:00 | 4872.4 | 46.88% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
