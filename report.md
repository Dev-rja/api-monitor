# API Reliability Monitor — SLA Report

> Last updated: **2026-04-23 16:06 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **79.2%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 61.25% | 4094.1 | 10206.7 | 1000ms | 174/449 |
| ❌ | `public_apis_list` | 0.0% | 99.55% | 128.9 | 4088.9 | 1500ms | 2/449 |
| ❌ | `nasa_apod` | 61.47% | 36.75% | 4411.1 | 10549.1 | 2000ms | 284/449 |
| ❌ | `ipapi_check` | 93.54% | 100.0% | 158.3 | 353.0 | 2500ms | 0/449 |
| ⚠️ | `open_meteo_weather` | 98.22% | 96.88% | 742.1 | 14877.1 | 2000ms | 14/449 |
| ⚠️ | `rest_countries` | 98.44% | 98.0% | 364.3 | 10221.5 | 2500ms | 9/449 |
| ⚠️ | `dog_ceo_random` | 99.33% | 90.65% | 842.3 | 10244.1 | 2500ms | 42/449 |
| ✅ | `catfact_random` | 99.33% | 99.33% | 269.1 | 10080.2 | 3000ms | 3/449 |
| ✅ | `useless_fact` | 99.55% | 99.11% | 584.8 | 10229.6 | 2500ms | 4/449 |
| ✅ | `agify_name` | 100.0% | 99.78% | 374.8 | 3237.1 | 2000ms | 1/449 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.78% | 233.4 | 2314.9 | 2000ms | 1/449 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 100.8 | 252.0 | 1500ms | 0/449 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `numbers_trivia` | 00:00 | 6402.8 | 62.5% |
| `nasa_apod` | 17:00 | 6132.0 | 73.08% |
| `nasa_apod` | 03:00 | 5851.5 | 84.62% |
| `nasa_apod` | 18:00 | 5700.0 | 84.21% |
| `nasa_apod` | 00:00 | 5195.1 | 75.0% |
| `nasa_apod` | 11:00 | 5177.6 | 62.96% |
| `nasa_apod` | 01:00 | 4971.7 | 60.0% |
| `numbers_trivia` | 10:00 | 4947.7 | 47.62% |
| `numbers_trivia` | 12:00 | 4944.8 | 47.37% |
| `nasa_apod` | 21:00 | 4923.2 | 56.0% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
